import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# 1. Load the data
df = pd.read_csv('data/apple_stock_latest.csv', index_col='Date', parse_dates=True)

# 2. Visualise the raw price
plt.figure(figsize=(10, 5))
plt.plot(df['Close'], label='AAPL Close Price')
plt.title('Apple Stock Price (2021 - 2026)')
plt.legend()
plt.show()

# 3. Perform the Augmented Dickey-Fuller (ADF) Test
print("--- Augmented Dickey-Fuller Test ---")
result = adfuller(df['Close'])
print(f'ADF Statistic: {result[0]:.4f}')
print(f'p-value: {result[1]:.4f}')

if result[1] <= 0.05:
    print("Result: Data is stationary (Reject H0)")
else:
    print("Result: Data is non-stationary (Fail to reject H0). Transformation needed.")