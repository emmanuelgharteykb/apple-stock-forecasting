import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# 1. Load data
df = pd.read_csv('data/apple_stock_latest.csv', index_col='Date', parse_dates=True)
df_diff = df['Close'].diff().dropna()

# 2. Plot ACF and PACF
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

plot_acf(df_diff, lags=20, ax=ax1)
ax1.set_title("Autocorrelation (ACF) - Helps find 'q'")

plot_pacf(df_diff, lags=20, ax=ax2)
ax2.set_title("Partial Autocorrelation (PACF) - Helps find 'p'")

plt.tight_layout()
plt.show()