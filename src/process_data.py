import pandas as pd
from src.data_loader import load_data
from src.config import COINS

def merge_datasets():
    """
    Reads all raw CSVs and merges them into a single DataFrame.
    """
    # 1. Create an empty DataFrame to hold everything
    master_df = pd.DataFrame()

    for coin in COINS:
        print(f"Processing {coin}...")
        
        # A. Load the data using your new function
        filename = f"data/raw/{coin}_raw.csv"
        df = load_data(filename)

        # B. Rename the 'price' column to f"{coin}_price"
        df.rename(columns={"price": f"{coin}_price"}, inplace=True)
        
        # C. Join to master_df
        if master_df.empty:
            master_df = df
        else:
            # We join on the 'Index' (the timestamp)
            master_df = master_df.join(df, how="outer")
            
    return master_df

if __name__ == "__main__":
    df = merge_datasets()
    print(df.head())
    print(df.info())
    # Save it later...
    # Save the Master Dataset
    df.to_csv("data/processed/merged_prices.csv")
    print("Saved merged data!")