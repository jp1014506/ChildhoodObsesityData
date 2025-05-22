import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, shapiro, levene
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load dataset
df = pd.read_csv('Nutrition__Physical_Activity__and_Obesity_-_Youth_Risk_Behavior_Surveillance_System.csv')

# Data preparation
df = df.dropna(subset=['Data_Value'])  # Drop rows with missing Data_Value
df['Data_Value'] = pd.to_numeric(df['Data_Value'], errors='coerce')  # Ensure Data_Value is numeric

# Filter dataset to only include rows where the question is about obesity
df_obesity = df[df['Question'] == "Percent of students in grades 9-12 who have obesity"]

# Ensure df_obesity has valid data
if df_obesity.empty:
    raise ValueError("Filtered dataset is empty. Check if the 'Question' column contains the specified text.")

# === Step 1: Generate Bar Graphs for Multiple Years ===
# Determine the most recent years with the most complete data
year_counts = df_obesity['YearStart'].value_counts().sort_values(ascending=False)
most_complete_years = year_counts.head(4).index.tolist()  # Top 4 years with most data

# Create bar graphs for the selected years
bar_chart_paths = []
for year in most_complete_years:
    df_year = df_obesity[df_obesity['YearStart'] == year]
    obesity_data_state = df_year.groupby('LocationDesc')['Data_Value'].mean().sort_values(ascending=False)

    # Plot bar graph
    plt.figure(figsize=(12, 8))
    sns.barplot(x=obesity_data_state.index, y=obesity_data_state.values)
    plt.title(f'Childhood Obesity Rates in {year} by State')
    plt.xlabel('State')
    plt.ylabel('Average Obesity Rate (%)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    bar_chart_path = f'obesity_bar_chart_{year}.png'
    plt.savefig(bar_chart_path)
    bar_chart_paths.append(bar_chart_path)
    plt.close()

# === Step 2: Pie Chart for Most Recent Year ===
# Use the most recent year with complete data
most_recent_year = most_complete_years[0]
df_recent_year = df_obesity[df_obesity['YearStart'] == most_recent_year]

# Aggregate data for the pie chart and exclude "National"
obesity_data_state = df_recent_year.groupby('LocationDesc')['Data_Value'].mean().sort_values(ascending=False)
obesity_data_state = obesity_data_state[obesity_data_state.index != 'National']

# Plot pie chart
plt.figure(figsize=(12, 12))
plt.pie(obesity_data_state, labels=obesity_data_state.index, autopct=lambda pct: f'{pct:.1f}%', startangle=90,
        pctdistance=0.85)  # Adjust distance of labels
plt.title(f'Obesity Rate Distribution by State in {most_recent_year}')
plt.axis('equal')
plt.tight_layout()
pie_chart_path = 'obesity_pie_chart.png'
plt.savefig(pie_chart_path)
plt.close()

# === Step 3: Statistical Tests ===
# Normality test for obesity rates by year
normality_results = ""
for year in df_obesity['YearStart'].unique():
    year_data = df_obesity[df_obesity['YearStart'] == year]['Data_Value']
    if len(year_data) >= 3:  # Ensure enough data points for the test
        stat, p = shapiro(year_data)
        normality_results += f"Year {year}: Statistic = {stat}, p-value = {p}\n"

# Levene's test for homogeneity of variance
levene_stat, levene_p = levene(*[df_obesity[df_obesity['YearStart'] == year]['Data_Value'] for year in df_obesity['YearStart'].unique()])
levene_results = f"Levene's Test for Homogeneity of Variance: Statistic = {levene_stat}, p-value = {levene_p}\n"

# ANOVA and Tukey's Test by Year
anova_years_stat, anova_years_p = f_oneway(*[df_obesity[df_obesity['YearStart'] == year]['Data_Value'] for year in df_obesity['YearStart'].unique()])
tukey_years = pairwise_tukeyhsd(endog=df_obesity['Data_Value'], groups=df_obesity['YearStart'], alpha=0.05)

# ANOVA and Tukey's Test by State
states = df_obesity['LocationDesc'].unique()
anova_states_data = [df_obesity[df_obesity['LocationDesc'] == state]['Data_Value'] for state in states]
anova_states_stat, anova_states_p = f_oneway(*anova_states_data)
tukey_states = pairwise_tukeyhsd(endog=df_obesity['Data_Value'], groups=df_obesity['LocationDesc'], alpha=0.05)

# === Step 4: Save All Results into a Single File ===
with open("analysis_results.txt", "w") as f:
    f.write(f"=== Analysis for {most_recent_year} ===\n")
    f.write(f"Pie chart saved at: {pie_chart_path}\n")
    f.write("=== Bar Graphs ===\n")
    f.write(f"Generated bar graphs for years: {', '.join(map(str, most_complete_years))}\n")
    for path in bar_chart_paths:
        f.write(f"Bar graph saved at: {path}\n")

    f.write("\n=== Normality Test Results (Shapiro-Wilk) ===\n")
    f.write(normality_results + "\n")

    f.write("=== Levene's Test for Homogeneity of Variance ===\n")
    f.write(levene_results + "\n")

    f.write("=== ANOVA by Year ===\n")
    f.write(f"F-statistic = {anova_years_stat}, p-value = {anova_years_p}\n")
    f.write("=== Tukey's Test for Yearly Differences ===\n")
    f.write(str(tukey_years) + "\n\n")

    f.write("=== ANOVA by State ===\n")
    f.write(f"F-statistic = {anova_states_stat}, p-value = {anova_states_p}\n")
    f.write("=== Tukey's Test for State Differences ===\n")
    f.write(str(tukey_states) + "\n")

print("Analysis complete. Results and graphs saved.")
