import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('data_management/Casual_Inference_Exp_Data.csv')

# Step 1: Data Preparation
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str).str.zfill(2) + '-01')
df['Did'] = df['Group'] * df['Event']

# Create seasonal dummies
for month in range(1, 13):
    df[f'Month_{month}'] = (df['Month'] == month).astype(int)

# Step 2: Basic DiD Model
basic_model = ols('Boardings ~ Group + Event + Did', data=df).fit()
print("Basic DiD Model Results:")
print(basic_model.summary())

# Step 3: Advanced DiD Model with Controls
advanced_model = ols('''Boardings ~ Group + Event + Did +
                        Population + Employment_Rate + Gas_Price + Mean_Temp +
                        Month_2 + Month_3 + Month_4 + Month_5 + Month_6 + 
                        Month_7 + Month_8 + Month_9 + Month_10 + Month_11 + Month_12''',
                     data=df).fit()
print("\nAdvanced DiD Model Results:")
print(advanced_model.summary())

# Step 4: Visualizing the DiD Effect
plt.figure(figsize=(12, 6))
for group in [0, 1]:
    group_data = df[df['Group'] == group]
    plt.scatter(group_data['Date'], group_data['Boardings'],
                label=f"{'Calgary' if group else 'Vancouver'} ({'Treatment' if group else 'Control'})",
                alpha=0.6)

    # Fit and plot trend lines
    for event in [0, 1]:
        event_data = group_data[group_data['Event'] == event]
        z = np.polyfit(event_data['Date'].astype(int) / 10 ** 9, event_data['Boardings'], 1)
        p = np.poly1d(z)
        plt.plot(event_data['Date'], p(event_data['Date'].astype(int) / 10 ** 9),
                 linestyle='--' if event else '-')

plt.axvline(x=pd.to_datetime('2016-12-01'), color='r', linestyle='--', label='Uber Introduction')
plt.title("DiD Visualization: Public Transport Boardings Over Time")
plt.xlabel("Date")
plt.ylabel("Boardings")
plt.legend()
plt.show()

# Step 5: Parallel Trends Assumption Check
df['Days'] = (df['Date'] - df['Date'].min()).dt.days  # Convert date to numeric

pre_uber = df[df['Event'] == 0]
control_trend = sm.OLS.from_formula('Boardings ~ Days', data=pre_uber[pre_uber['Group'] == 0]).fit()
treatment_trend = sm.OLS.from_formula('Boardings ~ Days', data=pre_uber[pre_uber['Group'] == 1]).fit()

print("\nPre-Uber Trends:")
print(f"Control (Vancouver) slope: {control_trend.params['Days']:.4f}")
print(f"Treatment (Calgary) slope: {treatment_trend.params['Days']:.4f}")
print(f"Slope difference: {treatment_trend.params['Days'] - control_trend.params['Days']:.4f}")

# Step 6: Placebo Test
df['Placebo_Event'] = (df['Date'] >= '2015-12-01').astype(int)
df['Placebo_Did'] = df['Group'] * df['Placebo_Event']

placebo_model = ols('''Boardings ~ Group + Placebo_Event + Placebo_Did +
                       Population + Employment_Rate + Gas_Price + Mean_Temp +
                       Month_2 + Month_3 + Month_4 + Month_5 + Month_6 + 
                       Month_7 + Month_8 + Month_9 + Month_10 + Month_11 + Month_12''',
                    data=df[df['Date'] < '2015-01-01']).fit()
print("\nPlacebo Test Results:")
print(placebo_model.summary())

# Step 7: Heterogeneous Effects
df['High_Population'] = (df['Population'] > df['Population'].median()).astype(int)
heterogeneous_model = ols('''Boardings ~ Group + Event + Did + Did:High_Population +
                           Population + Employment_Rate + Gas_Price + Mean_Temp +
                           Month_2 + Month_3 + Month_4 + Month_5 + Month_6 + 
                           Month_7 + Month_8 + Month_9 + Month_10 + Month_11 + Month_12''',
                          data=df).fit()
print("\nHeterogeneous Effects Model Results:")
print(heterogeneous_model.summary())

# Visualize Heterogeneous Effects
plt.figure(figsize=(10, 6))
effects = [heterogeneous_model.params['Did'], heterogeneous_model.params['Did:High_Population']]
errors = [heterogeneous_model.bse['Did'], heterogeneous_model.bse['Did:High_Population']]
plt.bar(['Average Effect', 'Additional Effect for High Population'], effects, yerr=errors, capsize=5)
plt.title('Heterogeneous Effects of Uber on Public Transport Boardings')
plt.ylabel('Effect Size')
plt.show()

# Step 8: Long-term Effects
df['Years_Since_Uber'] = (df['Date'].dt.year - 2016) * df['Event']
df['Years_Since_Uber'] = df['Years_Since_Uber'].clip(lower=0)
long_term_model = ols('''Boardings ~ Group + Event + Did + Years_Since_Uber +
                           Population + Employment_Rate + Gas_Price + Mean_Temp +
                           Month_2 + Month_3 + Month_4 + Month_5 + Month_6 + 
                           Month_7 + Month_8 + Month_9 + Month_10 + Month_11 + Month_12''',
                      data=df).fit()
print("\nLong-term Effects Model Results:")
print(long_term_model.summary())

# Visualize Long-term Effects
plt.figure(figsize=(10, 6))
years = range(6)  # 0 to 5 years after Uber introduction
effects = [long_term_model.params['Did'] + year * long_term_model.params['Years_Since_Uber'] for year in years]
plt.plot(years, effects, marker='o')
plt.title('Estimated Long-term Effects of Uber on Public Transport Boardings')
plt.xlabel('Years Since Uber Introduction')
plt.ylabel('Estimated Effect')
plt.show()
