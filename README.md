This report and subsequent code was part of a Data Science project I work on in class.  I looked at nation-wide data regarding childhood obesity, activity levels and eating habits, running statistical analysis on the different factors and variables that shape the data.

Final Report: Analysis of Childhood Obesity Trends
Across the United States
Introducon*
Childhood obesity remains a pressing public health concern in the United States. To be9er
understand its trends, this report analyzes state-wise and year-wise obesity rates among
children using the Youth Risk Behavior Surveillance System dataset from the website Data.gov.
StaAsAcal tests and visualizaAons were used to invesAgate differences across states and years,
as well as highlight overall trends.

This analysis focuses on the following quesAons:

Are there staAsAcally significant differences in obesity rates across years?
Are there staAsAcally significant differences in obesity rates across states?
What insights can be derived from visualizing these trends using bar and pie charts?
Methods
The dataset includes state-level percentages of childhood obesity rates recorded over mulAple
years. Data preparaAon involved:

Removing rows with missing obesity rate values (Data_Value).
Ensuring numeric formaRng for calculaAons and staAsAcal tests.
SelecAng data that is refers to the quesAon “Percent of students in grades 9-12 who
have obesity”
The following analyses and visualizaAons were performed:
Pie Chart : Displays the proporAon of childhood obesity rates by state for the for the year
of 2021, chosen for its completeness of data and the most recent year complete data
was available.
Bar Charts : Show childhood obesity rates across states for the four most complete years,
highlighAng trends over Ame. They are fortunately are spaced out between the years
2011 - 2021.
Stascal Tests** :
o ANOVA and Tukey's HSD tests assessed differences in obesity rates across years
and states.
o Normality (Shapiro-Wilk) and Variance Homogeneity (Levene’s Test) checks
were performed to validate assumpAons for ANOVA.
Hypotheses
For the hypotheses of the tests, they will be assigned in blocks for tests that are as
follows:

1) Shapiro-Wilk Tests on the Years:
H 0 : The data for that specific year follows a normal distribuAon.
H 1 : The data for that specific year does not follow a normal distribuAon.
2) Levene’s Tests on the Years:
H 0 : The variance across all years is equal.
H 1 : The variance across all years is not equal.
3) ANOVA by Year
H 0 : The mean obesity rate across years is the same.
H 1 : The mean obesity rate across years is the not same.
4) Tukey’s by Year
H 0 : The mean obesity rate between each pair of years is the same.
H 1 : The mean obesity rate between each pair of years is the not same.
5) ANOVA by State
H 0 : The mean obesity rate across states is the same.
H 1 : The mean obesity rate across states is the not same.
6) Tukey’s by State
H 0 : The mean obesity rate between each pair of states is the same.
H 1 : The mean obesity rate between each pair of states is the not same.
Visualizaons*

Pie Chart :
The pie chart, based on data from the most recent complete year ( 2021 ), illustrates the
proporAon of childhood obesity rates a9ributed to each state. The NaAonal average was
excluded to focus on state contribuAons to the naAonal total. States with higher obesity
rates contributed a more significant proporAon, while smaller states collecAvely
represented a minor share.
Bar Charts :
Four bar charts were generated for the years with the most complete data: 2011 , 2017 ,
2019 , and 2021. These visualizaAons reveal fluctuaAons in obesity rates by state,
indicaAng that some states consistently rank higher than others, while some rankings
rise and fall.
Stascal Analyses**

Normality and Homogeneity of Variance
o Shapiro-Wilk Test : Data for obesity rates across years and states deviated from
normality (p-values < 0.05).
o Levene's Test : Variance across groups was heterogeneous (p-value < 0.05).
These results suggest cauAon when interpreAng ANOVA, though it remains robust for
moderately non-normal data with unequal variances in large datasets.
ANOVA and Tukey's HSD
o Across Years :
§ ANOVA showed significant differences in obesity rates across years ( F-
stasc = 92.19633443700475, p-value = 1.3487981553505422e- 174** ).
§ Tukey's HSD idenAfied a majority of specific year-pairs with significant
differences, indicaAng an upward trend in some states and a leveling off
in others.
o Across States :
§ ANOVA confirmed staAsAcally significant differences between states ( F-
sta*s*c = 31.36966774213451, p-value = 6.902862496880047e- 256 ).
§ Tukey's HSD revealed that a substanAal amount, enough to reject the null
hypothesis in most cases, of State-State pairs demonstrated a staAsAcally
significant difference. Since there is so much data, more analysis can be
performed to find differences between the individual states as well.
Discussion
The analysis underscores significant dispariAes in childhood obesity rates both temporally and
geographically.

Temporal Trends :
o The bar charts highlight noAceable changes in obesity rates over the selected
years. Some states experienced gradual changes, while others showed
stabilizaAon or minor changes.
o StaAsAcal tests confirmed these differences, indicaAng the need for further
analysis.
o Some states show a clear trends of being the heaviest or least-heaviest states,
with these trends lasAng upwards of a decade.
Geographical Pa\erns :
o Both the pie chart and bar graphs emphasize the disproporAonate burden of
childhood obesity in certain states, parAcularly in the South and Midwest
regions. These areas consistently recorded the highest rates over Ame. States
and territories that are economically depressed also shared this characterisAc.
Policy Implicaons* :
o This data highlights the importance of state-specific strategies to address
childhood obesity. Investments in educaAon, access to nutriAous foods, and
physical acAvity programs may yield significant public health benefits.
o It is also useful to examine which states have successful child-health policies, and
which ones could improve or miAgate the effect of societal and environmental
effects.
Literature Review
Morrill and Chinn examined the relaAonship between behavioral and environmental
factors influencing childhood obesity in their paper, The Obesity Epidemic in the United States.
They idenAfied key contributors such as the amount of Ame spent watching television, whether
schools mandated physical educaAon, and the availability of vending machines or fast-food
restaurants. These factors, they argued, funcAon at a societal level where state policies play a
criAcal role in shaping outcomes (Morrill, 2004). Their findings suggest that states addressing
these factors through policy intervenAons are more likely to see improved health outcomes,
while others that neglect these issues conAnue to face significant challenges.
In The Social and Emo=onal Lives of Overweight, Obese, and Severely Obese Children ,
Harrist et al. explored the emoAonal impact of obesity on children. The study highlighted the
role of environmental and demographic factors, noAng, “Second, the sample was gathered from

rural elementary schools with a relaAvely large proporAon of NaAve American students, both
risk factors for obesity” (Harrist, 2016). This aligns with my staAsAcal analysis, which indicates
that rural states, such as West Virginia, Mississippi, Texas, and Ohio, rank among the highest in
childhood obesity rates. West Virginia, in parAcular, exemplifies this trend, with its rural
demographics contribuAng significantly to its high obesity rates.
A related global perspecAve is provided in an arAcle from The Economist , Atled “Why the
War on Childhood Obesity Is Failing.” The author reports that “[s]ince 1990 global rates have
doubled among adults and quadrupled among children” (The Economist, 2024). This finding
underscores the rapid and widespread nature of the obesity epidemic, parAcularly in
developing countries. My analysis supports this claim, demonstraAng a consistent upward trend
in U.S. childhood obesity rates over the past decade. While the data primarily reflects trends in
the United States, it aligns with global pa9erns, highlighAng the broader implicaAons of the
obesity crisis.

Conclusion
This report underscores the importance of data-driven insights in addressing childhood
obesity. Through visualizaAons and staAsAcal analyses, it provides a clearer understanding of
trends across states and years, emphasizing the need for targeted intervenAons. Future
research should invesAgate behavioral and demographic factors to further idenAfy the root
causes of these dispariAes.
The analysis reveals staAsAcally significant differences between states and years,
indicaAng that childhood obesity is not only evolving over Ame but also shaped by state-level
policies and environmental factors. Over the past decade, childhood obesity has steadily
increased, as evidenced by the growing range of values in bar graph visualizaAons.
For example, West Virginia’s progression highlights the severity of this issue: the state
ranked 13th in childhood obesity in 2011, 5th in 2017, 2nd in 2019, and 1st in 2021. By 2021,
West Virginia had the highest percentage of obese children in the United States at 3.5%. These
trends are further supported by detailed staAsAcal analyses and visual representaAons, such as
those found in the analysis_results.txt file, which provides deeper insights into these pa9erns.
Although many of the Shapiro-Wilk normality tests produced p-values indicaAng non-
normal distribuAons, the ANOVA tests remained appropriate due to the dataset's size. While the
validity of these tests may have some limitaAons, the visualizaAons effecAvely highlight
significant trends, providing acAonable insights despite potenAal imperfecAons.

Bibliography and Appendix

Centers for Disease Control and Prevenon.* (n.d.). Nutri=on, Physical Ac=vity, and Obesity -
Youth Risk Behavior Surveillance System. Data.gov. Retrieved from
h9ps://catalog.data.gov/dataset/nutriAon-physical-acAvity-and-obesity-youth-risk-
behavior-surveillance-system
Harrist, A. W., Swindle, T. M., Hubbs-Tait, L., Topham, G. L., Shriver, L. H., & Page, M. C. (2016).
The social and emoAonal lives of overweight, obese, and severely obese children. Child
Development, 87 (5), 1564–1580. h9ps://www.jstor.org/stable/

Morrill, A. C., & Chinn, C. D. (2004). The obesity epidemic in the United States. Journal of Public
Health Policy, 25 (3/4), 353–366. h9ps://doi.org/10.1057/palgrave.jphp.
The Economist. (2024, August 8). Why the war on childhood obesity is failing. The Economist.
