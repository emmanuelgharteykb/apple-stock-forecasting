import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

# 1. Load the saved results safely
try:
    # We load without setting the index first to see what columns we actually have
    test = pd.read_csv('data/test_results.csv')
    forecast_df = pd.read_csv('data/forecast_results.csv')

    # Rename the first column to 'Date' if it's unnamed (common when saving index)
    if 'Unnamed: 0' in test.columns:
        test.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)
    if 'Unnamed: 0' in forecast_df.columns:
        forecast_df.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)

    # Now set the index
    test.set_index('Date', inplace=True)
    forecast_df.set_index('Date', inplace=True)

    actual_prices = test['Close']
    predicted_prices = forecast_df['mean']

    # 2. Calculate Metrics
    rmse = np.sqrt(mean_squared_error(actual_prices, predicted_prices))
    mape = np.mean(np.abs((actual_prices - predicted_prices) / actual_prices)) * 100

    print(f"--- Evaluation Metrics ---")
    print(f"RMSE: ${rmse:.2f}")
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")

except FileNotFoundError:
    print("Error: CSV files not found. Make sure you ran the forecast script first!")
except KeyError as e:
    print(f"Error: Could not find column {e}. Check your CSV headers.")