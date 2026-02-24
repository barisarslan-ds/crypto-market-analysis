import requests
import pandas as pd
from src.config import COINGECKO_BASE_URL, DAYS, CURRENCY

def fetch_coin_data(coin_id):
    """
    Fetches historical market data for a specific coin from CoinGecko.
    
    Args:
        coin_id (str): The ID of the coin (e.g., 'bitcoin').
        
    Returns:
        pd.DataFrame: A DataFrame containing 'timestamp' and 'price'.
    """
    # 1. API Endpoint Construction
    # URL pattern: /coins/{id}/market_chart
    # Parameters: vs_currency=usd, days=365
    
    endpoint = f"{COINGECKO_BASE_URL}/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": CURRENCY,
        "days": DAYS
    }
    
    # Send the request to CoinGecko
    try:
        response = requests.get(endpoint, params=params)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {coin_id}: {e}")
        return None
    
    # Check for success (HTTP 200)
    if response.status_code == 200:
        data = response.json()
        prices = data.get('prices', []) # Safely get prices
        
        # Create DataFrame with clear columns
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        return df
    else:
        print(f"Failed to fetch {coin_id}: Status {response.status_code}")
        return None 

def load_data(filepath):
    """
    Reads a CSV file, parses dates, and sets the index.
    """
    # TODO: pd.read_csv() with parse_dates parameter
    df = pd.read_csv(filepath, parse_dates=["timestamp"])
    # TODO: set_index('timestamp')
    df.set_index("timestamp", inplace=True)
    return df

if __name__ == "__main__":
    # Test the function
    df = fetch_coin_data("bitcoin")
    print(df.head())
