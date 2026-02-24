import pandas as pd


df = pd.read_csv("data/processed/cleaned_prices.csv", index_col="timestamp")
df.index = pd.to_datetime(df.index, unit='ms')
df_weekly = df.resample("W").mean()

print("\nWeekly Data Head:")
print(df_weekly.head())

df_weekly.to_csv("data/processed/weekly_prices.csv")
print("✅ Saved weekly data!")