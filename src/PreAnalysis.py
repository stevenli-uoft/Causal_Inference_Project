import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy import stats
import seaborn as sns

df = pd.read_csv('Casual_Inference_Exp_Data.csv')

# Convert 'Year' and 'Month' to datetime
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str).str.zfill(2) + '-01')

# Filter data for pre-Uber period (Uber was introduced in December 2016)
pre_uber = df[df['Date'] < '2016-12-01']

# Separate data for Calgary (Group 1) and Vancouver (Group 0)
calgary_data = pre_uber[pre_uber['Group'] == 1]['Boardings']
vancouver_data = pre_uber[pre_uber['Group'] == 0]['Boardings']

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Normalize the data using MinMaxScaler
calgary_norm = scaler.fit_transform(calgary_data.values.reshape(-1, 1)).flatten()
vancouver_norm = scaler.fit_transform(vancouver_data.values.reshape(-1, 1)).flatten()

# Plot the normalized trends
plt.figure(figsize=(12, 6))
plt.plot(pre_uber[pre_uber['Group'] == 0]['Date'].unique(), vancouver_norm, label='Vancouver (normalized)')
plt.plot(pre_uber[pre_uber['Group'] == 1]['Date'].unique(), calgary_norm, label='Calgary (normalized)')
plt.title('Parallel Trends Check: Normalized Boardings (Pre-Uber, before Dec-2016)')
plt.xlabel('Year')
plt.ylabel('Normalized Boardings')
plt.legend()
plt.show()

# Calculate and print the trend difference
trend_diff = np.mean(np.abs(calgary_norm - vancouver_norm))
print(f"Average trend difference: {trend_diff:.4f}")

# Calculate the difference in slopes
calgary_slope = np.polyfit(range(len(calgary_norm)), calgary_norm, 1)[0]
vancouver_slope = np.polyfit(range(len(vancouver_norm)), vancouver_norm, 1)[0]
slope_diff = calgary_slope - vancouver_slope

# Perform a t-test on the difference in slopes
t_stat, p_value = stats.ttest_ind(calgary_norm, vancouver_norm)

print(f"Slope difference: {slope_diff:.4f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Optional: Time series plot of boardings
plt.figure(figsize=(12, 6))
for group in [0, 1]:
    group_data = df[df['Group'] == group]
    plt.plot(group_data['Date'], group_data['Boardings'],
             label='Vancouver' if group == 0 else 'Calgary')
plt.axvline(x=pd.to_datetime('2016-12-01'), color='r', linestyle='--', label='Uber Introduction')
plt.title('Public Transport Boardings Over Time')
plt.xlabel('Date')
plt.ylabel('Boardings')
plt.legend()
plt.show()

# Optional: Correlation heatmap
correlation_vars = ['Boardings', 'Population', 'Employment_Rate', 'Gas_Price', 'Mean_Temp']
correlation_matrix = df[correlation_vars].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Heatmap of Key Variables')
plt.tight_layout()
plt.show()
