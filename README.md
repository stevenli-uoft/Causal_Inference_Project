# The Impact of Uber on Public Transportation: A Causal Inference Study

## Project Overview

This project investigates the causal effect of Uber's introduction on public transportation usage in Calgary. Uber was introduced to Calgary in December 2016, so this study employs a Difference-in-Differences (DiD) approach to analyze the impact from 2010 to 2019, using Calgary as the treamment city and Vancouver as the control city (Uber was introduced to Vancouver in 2020).

## Data

The dataset includes:
- Monthly public transport boardings for Calgary (2010-2019) [Source](https://data.calgary.ca/Transportation-Transit/Yearly-Ridership-current-year-is-year-to-date-/n9it-gzsq)
- Annual public transport boardings for Vancouver (2010-2019, extrapolated to monthly) [Source](https://www.translink.ca/plans-and-projects/data-and-information/accountability-centre/ridership)
- Monthly population (15+), labor force, employment rate, and unemployment rate for both cities [Source](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410029401&pickMembers%5B0%5D=2.5&pickMembers%5B1%5D=3.1&pickMembers%5B2%5D=4.2&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2010&cubeTimeFrame.endMonth=01&cubeTimeFrame.endYear=2020&referencePeriods=20100101%2C20200101)
- Monthly gas prices for both cities [Source](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000101&pickMembers%5B0%5D=2.2&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2010&cubeTimeFrame.endMonth=12&cubeTimeFrame.endYear=2020&referencePeriods=20100101%2C20201201)
- Monthly mean temperature and total precipitation for both cities [Source](https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2008-12-22%7C2024-08-10&dlyRange=1999-05-01%7C2024-08-09&mlyRange=2000-06-01%7C2007-11-01&StationID=27211&Prov=AB&urlExtension=_e.html&searchType=stnProx&optLimit=yearRange&StartYear=2010&EndYear=2020&selRowPerPage=25&Line=4&txtRadius=25&optProxType=city&selCity=51%7C2%7C114%7C4%7CCalgary&selPark=&txtCentralLatDeg=&txtCentralLatMin=0&txtCentralLatSec=0&txtCentralLongDeg=&txtCentralLongMin=0&txtCentralLongSec=0&txtLatDecDeg=&txtLongDecDeg=&timeframe=2&Day=11&Year=2019&Month=12#)

## Methodology

We employ a Difference-in-Differences (DiD) approach, treating Calgary as the intervention city and Vancouver as the control. The analysis includes:

1. Pre-analysis: Exploratory Data Analysis (EDA) and parallel trends assumption check
2. Basic DiD model
3. Advanced DiD model with control variables
4. Robustness checks: Placebo tests, parallel trends assumption re-check, heterogeneous effects analysis, and long-term effects analysis

## Pre-Analysis Results

### Parallel Trends Assumption Check

![Parallel_Trend_Test](https://github.com/user-attachments/assets/108b7583-cd9b-4fef-8f9a-70a786dfd8d6)

The visualization shows normalized boardings for Vancouver and Calgary from 2010 to end of 2016. The parallel trends assumption is reasonably satisfied, with both cities showing similar patterns and fluctuations in public transport usage before Uber's introduction.

### Exploratory Data Analysis

![Boardings_over_time](https://github.com/user-attachments/assets/1a201a69-94be-4311-adb4-cc7359d45988)

Key observations:
- Vancouver consistently has higher ridership than Calgary
- Both cities show seasonal fluctuations in ridership
- There's a noticeable upward trend in Vancouver's ridership over time
- Calgary's ridership remains relatively stable with slight fluctuations

### Correlation Analysis

![correlation_heatmap](https://github.com/user-attachments/assets/544264a6-1da2-4422-a1f1-0da95198decb)

Key findings:
- Strong positive correlation (0.98) between Boardings and Population
- Strong negative correlation (-0.83) between Boardings and Employment Rate
- Moderate positive correlation (0.76) between Boardings and Gas Price
- Weak to moderate positive correlation (0.39) between Boardings and Mean Temperature

## DiD Analysis Results

### Basic DiD Model

The basic Difference-in-Differences model provides a straightforward estimation of Uber's impact on public transport usage:

- Effect Size (DiD Coefficient): -7,254,000 boardings
- Statistical Significance: Highly significant (p < 0.001)
- Model Fit: R-squared = 0.967 (96.7% of variance explained)

The introduction of Uber is associated with a decrease of approximately 7.25 million public transport boardings in Calgary compared to Vancouver. This effect is both practically large and statistically significant. In other words, after Uber started operating, Calgary saw about 7.25 million fewer public transit trips than we would have expected based on the trends in Vancouver.

### Advanced DiD Model

The advanced model incorporates additional factors to provide a more nuanced understanding:

- Effect Size (DiD Coefficient): -4,979,000 boardings
- Statistical Significance: Highly significant (p < 0001)
- Model Fit: R-squared = 0.975 (97.5% of variance explained)

Even after accounting for factors like population, employment rate, gas prices, and seasonal effects, we still see a substantial impact from Uber's introduction. The model suggests that Uber's presence is associated with a decrease of about 4.98 million public transport boardings.
The smaller effect size in the advanced model (compared to the basic model) indicates that some of the changes in public transport usage are explained by these other factors. However, the persistent large and significant effect suggests that Uber had a real impact on public transit ridership.

To put this in perspective:

The effect represents a substantial portion of overall ridership.
It suggests that for every 10,000 trips that would have been taken on public transit before Uber, about 1,386 of these trips may have shifted to Uber or other alternatives after Uber's introduction (based on the advanced model's results).

![DiD_visualization](https://github.com/user-attachments/assets/70ff0688-c8f1-4ba8-82bf-450416d9a679)

This graph visually represents the divergence in public transport usage between Calgary and Vancouver after Uber's introduction. The gap between the two lines after the vertical dashed line (representing Uber's entry) illustrates the effect we've quantified in our models.
These findings provide strong evidence that the introduction of Uber had a significant negative impact on public transport usage in Calgary. 

However, it's important to note the divergent trends between Calgary and Vancouver after 2016. While Calgary's ridership remained relatively stagnant, Vancouver experienced a noticeable increase. This divergence could be attributed to factors such as increased public transport infrastructure development in Vancouver during this period. Such improvements typically lead to increased ridership by making public transit more accessible and efficient. This observation suggests that our DiD estimates might actually underestimate Uber's impact on Calgary's public transport usage. If Calgary had followed a similar upward trajectory to Vancouver in the absence of Uber, the difference in ridership would likely be even larger than our current estimates.

### Robustness Checks

1. Placebo Test:
   - DiD Coefficient: -1.188e-07
   - P-value: 0.901 (Not significant, supporting the validity of main results)

2. Heterogeneous Effects:
   - Interaction with High Population: 4.175e-07
   - P-value: 0.036 (Significant, indicating less negative effect in high-population areas)

3. Long-term Effects:
   - Years Since Uber Coefficient: 901,900
   - P-value: 0.003 (Significant, suggesting diminishing negative effect over time)

![longterm_effects](https://github.com/user-attachments/assets/5c7a3b9f-39d1-4cb4-adac-67985a358902)

## Key Findings

1. Uber's introduction is associated with a significant decrease in public transport usage in Calgary compared to Vancouver.
2. This effect persists even after controlling for various factors like population, employment rate, gas prices, and seasonal effects.
3. The impact of Uber appears to be less pronounced in areas with higher population.
4. Over time, the negative effect of Uber on public transport usage seems to diminish.

## Limitations and Future Work
- Due to Vancouver Boarding data being annual, it had to be extrapolated to monthly and estimated seasonality using recent trends as a proxy
- Imperfect parallel trends assumption
- Possible unaccounted factors influencing public transport usage, such as an increase in development for Vancouver public transportation infastructure
- Future work could include analyzing more cities or incorporating additional ride-sharing services
