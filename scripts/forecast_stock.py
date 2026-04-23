import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# 1. Load data
df = pd.read_csv('data/apple_stock_latest.csv', index_col='Date', parse_dates=True)
# Ensure we have a frequency set for the index (Business days)
df = df.asfreq('B').fillna(method='ffill')

# 2. Split into Train (all but last 10 days) and Test (last 10 days)
train = df.iloc[:-10]
test = df.iloc[-10:]

# 3. Fit the ARIMA(1, 1, 1) Model
# Order = (p, d, q) -> p=1 (AR), d=1 (Differencing), q=1 (MA)
model = SARIMAX(train['Close'], order=(1, 1, 1))
model_fit = model.fit(disp=False)

# 4. Forecast
forecast_steps = 10
forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_df = forecast.summary_frame()

# 5. Visualize
plt.figure(figsize=(12, 6))
plt.plot(train['Close'].tail(50), label='Historical (Train)')
plt.plot(test['Close'], label='Actual (Test)', color='green')
plt.plot(forecast_df['mean'], label='Forecast', color='red', linestyle='--')
plt.fill_between(forecast_df.index, forecast_df['mean_ci_lower'], 
                 forecast_df['mean_ci_upper'], color='pink', alpha=0.3)

plt.title('AAPL Stock Price Forecast vs Actual (April 2026)')
plt.legend()
plt.show()

print(model_fit.summary())