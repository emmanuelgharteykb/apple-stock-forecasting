import yfinance as yf
import pandas as pd
import os

def fetch_aapl_data():
    ticker = "AAPL"
    print(f"Fetching latest data for {ticker}...")
    
    # Downloading 5 years of data up to today
    df = yf.download(ticker, start="2021-01-01")
    
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Ensure the data folder exists
    os.makedirs('data', exist_ok=True)
    
    # Save the file
    df.to_csv('data/apple_stock_latest.csv')
    print(f"Successfully saved to data/apple_stock_latest.csv")
    print(f"Latest Close Price: ${df['Close'].iloc[-1]:.2f}")

if __name__ == "__main__":
    fetch_aapl_data()