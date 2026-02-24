from src.data_loader import fetch_coin_data
from src.config import COINS
import os

# Ensure the directory exists (just in case)
os.makedirs("data/raw", exist_ok=True)

for coin in COINS:
    print(f"Fetching data for {coin}...")
    df = fetch_coin_data(coin)
    
    if df is not None:
        filename = f"data/raw/{coin}_raw.csv"
        df.to_csv(filename, index=False)
        print(f"✅ Saved {coin} to {filename}")
    else:
        print(f"❌ Failed to fetch {coin}")