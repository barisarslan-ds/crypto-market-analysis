import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/returns.csv", index_col='timestamp')

corr_matrix = df.corr()
print(corr_matrix)

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Crypto Correlation Matrix")
plt.show()