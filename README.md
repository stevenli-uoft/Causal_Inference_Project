# The Impact of Uber on Taxi Rides: A Causal Inference Study

## Project Overview

This project investigates the causal effect of Uber's introduction on Taxi usage in Calgary. Uber was introduced to Calgary in December 2016, so this study employs a Difference-in-Differences (DiD) approach to analyze the impact from 2014 to 2018, using Calgary as the treamment city and Vancouver as the control city (Uber was introduced to Vancouver in 2020).

## Data

The dataset includes:
- Monthly taxi rides for Calgary and Vancouver (2014-2018)
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

![parellel_trend_test](https://github.com/user-attachments/assets/3c1db6e0-0e55-45d7-a67d-652009e46915)

The visualization shows normalized taxi rides for Vancouver and Calgary from 2014 to end of 2016. The parallel trends test results (p-value = 0.1083) suggest that the parallel trends assumption is reasonably satisfied, which is crucial for the validity of the DiD analysis.

### Exploratory Data Analysis

![taxi_rides_over_time](https://github.com/user-attachments/assets/6b803463-83bd-4b9b-a2c2-3248bf61fcd7)

Key observations:
- Vancouver consistently has higher taxi ridership than Calgary
- Both cities show seasonal fluctuations in ridership
- There's a noticeable downward trend in Calgary's ridership after Uber's introduction

### Correlation Analysis

![correlation_heatmap](https://github.com/user-attachments/assets/287c1c0e-70e2-4360-9803-0d0669b55a71)

Key findings:
- Strong positive correlation (0.98) between Rides and Population
- Strong negative correlation (-0.88) between Rides and Employment Rate
- Moderate positive correlation (0.69) between Rides and Gas Price
- Weak to moderate positive correlation (0.42) between Rides and Mean Temperature

## DiD Analysis Results

### Basic DiD Model

The basic Difference-in-Differences model provides a straightforward estimation of Uber's impact on taxi usage:

- Effect Size (DiD Coefficient): -51,030 rides
- Statistical Significance: Significant (p = 0.017)
- Model Fit: R-squared = 0.990 (99.0% of variance explained)

The introduction of Uber is associated with a decrease of approximately 51,000 taxi rides per month in Calgary compared to Vancouver. This effect is both practically large and statistically significant.

### Advanced DiD Model

The advanced model incorporates additional factors to provide a more nuanced understanding:

- Effect Size (DiD Coefficient): -51,490 rides
- Statistical Significance: Significant (p = 0.011)
- Model Fit: R-squared = 0.995 (99.5% of variance explained)

Even after accounting for factors like population, employment rate, gas prices, and seasonal effects, we still see a substantial impact from Uber's introduction. The model suggests that Uber's presence is associated with a decrease of about 51,500 taxi rides per month.

To put this in perspective:

The effect represents a substantial portion of overall taxi ridership in Calgary. Based on the advanced model's results, it suggests that for every 10,000 taxi rides that would have occurred before Uber's introduction, approximately 1,430 of these rides were likely displaced by Uber or other alternatives after Uber began operations. This indicates a significant shift in transportation choices, with over 14% of potential taxi trips being affected by the presence of ride-sharing services.

![DiD_Visualization](https://github.com/user-attachments/assets/88c2d749-323f-4022-86ad-e873bdc11083)

This graph visually represents the divergance in taxi usage between Calgary and Vacnouver after Uber's introduction. Although it may be difficult to visually notice the divergence, the DiD model provides strong evidence that the introduction of Uber had a significant negative impact on Taxi trip volumes in Calgary.

### Robustness Checks

1. Placebo Test:
   - DiD Coefficient: -9.222e-08
   - P-value: 0.869 (Not significant, supporting the validity of main results)

2. Heterogeneous Effects:
   - Interaction with High Population: 1.91e-07
   - P-value: < 0.001 (Significant, indicating less negative effect in high-population areas)

3. Long-term Effects:
   - Years Since Uber Coefficient: -25,580
   - P-value: 0.168 (Not significant, suggesting no strong evidence for changing effects over time)
  
![longterm_effects](https://github.com/user-attachments/assets/1381d8d7-3e99-438d-8164-0e1d45aaa908)

## Key Findings
1. Uber's introduction is associated with a significant decrease in taxi rides in Calgary compared to Vancouver, with an estimated reduction of about 51,000 rides per month.
2. This effect persists even after controlling for various factors like population, employment rate, gas prices, and seasonal effects.
3. The impact of Uber appears to be less pronounced in areas with higher population.
4. There's no strong evidence for changing effects over time, though there's a suggestion of potentially increasing negative effects.

## Limitations and Future Work
- Possible unaccounted factors influencing taxi usage in both cities
- Relatively short post-treatment period (2 years) limiting long-term effect analysis
- Future work could include analyzing more cities or incorporating additional ride-sharing services
- Consideration of city-specific events or policies that might affect taxi ridership
