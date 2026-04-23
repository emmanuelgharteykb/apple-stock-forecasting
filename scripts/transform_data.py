import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# 1. Load the data
df = pd.read_csv('data/apple_stock_latest.csv', index_col='Date', parse_dates=True)

# 2. Apply First-Order Differencing
df['Close_Diff'] = df['Close'].diff().dropna()

# 3. Visualize the Transformation
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(df['Close'], color='blue')
plt.title('Original Non-Stationary Data (Prices)')

plt.subplot(2, 1, 2)
plt.plot(df['Close_Diff'], color='orange')
plt.title('Stationary Data (Daily Price Changes)')
plt.tight_layout()
plt.show()

# 4. Run ADF Test on the Differenced Data
print("--- ADF Test on Differenced Data ---")
# We drop the first NaN value created by .diff()
result = adfuller(df['Close_Diff'].dropna())
print(f'ADF Statistic: {result[0]:.4f}')
print(f'p-value: {result[1]:.4e}') # Using scientific notation as it will be very small

if result[1] <= 0.05:
    print("Result: Data is now stationary! You can move to forecasting.")
else:
    print("Result: Still non-stationary. May need second-order differencing.")