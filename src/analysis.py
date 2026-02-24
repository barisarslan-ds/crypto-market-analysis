import pandas as pd

# 1. Load Data 
df = pd.read_csv("data/processed/cleaned_prices.csv", index_col='timestamp', parse_dates=['timestamp'])

# 2. Calculate Returns AND Save to Variable
returns = df.pct_change()

# 3. Drop Method 
returns = returns.dropna()

print("Volatility (Standard Deviation):")
print(returns.std())

returns.to_csv("data/processed/returns.csv")
print("✅ Saved returns data!")