import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # Add this to see the plot

df = pd.read_csv("data/processed/merged_prices.csv", index_col='timestamp', parse_dates=['timestamp'])

print("Before Cleaning:")
print(df.isnull().sum())

# 1. Forward Fill (The Magic Fix)
df_clean = df.ffill()

# 2. Check again (Should be 0)
print("\nAfter Cleaning:")
print(df_clean.isnull().sum())

# 3. Save the clean version
df_clean.to_csv("data/processed/cleaned_prices.csv")
print("✅ Saved cleaned data!")

# Optional: Show the heatmap to prove it's empty
sns.heatmap(df_clean.isnull(), cbar=False)
plt.show()