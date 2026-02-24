import pandas as pd

df = pd.read_csv("data/processed/cleaned_prices.csv", index_col="timestamp", parse_dates=["timestamp"])
df_change = df.diff()

df_change.columns = [f"{col}_change" for col in df_change.columns]

df_final = pd.concat([df, df_change], axis=1)


df_final.to_csv("data/processed/featured_prices.csv")
print("✅ Saved featured data!")
print(df_final.head())