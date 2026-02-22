#Pearson_Correlation demo

#Examples 
    # Lung Cancer -> Smoking
    # Rain -> Umbrella

# Important to know that correlation doesnt imply causation
    # For example, with correlation, we cant say if the rain caused the umbrella or if the umbrella caused the rain

# Pearson Correlation values (+1 = LARGE positive relationship, -1 = Large Negative relationship, 0 = no relationship)
# P-value (X > 0.1 no certanty in the result, < 0.1 weak certainty, < 0.05 moderate certainty in the result, < 0.001 strong certainty in the result) 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

corr_headers =  ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

numeric_cols = [
    "symboling", "normalized-losses", "wheel-base", "length", "width",
    "height", "curb-weight", "engine-size", "bore", "stroke",
    "compression-ratio", "horsepower", "peak-rpm",
    "city-mpg", "highway-mpg", "price"
]
file_path = "Demos/Excel_folder/auto.csv"
df = pd.read_csv(file_path, names = headers)

print("These are the unique values for \'drive-wheels\': ", df['drive-wheels'].unique())
print(df.dtypes)
print("\n")
# Ensure price is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['price'])

# Ensure peak-rmp is numeric
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df = df.dropna(subset=['horsepower'])


df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=numeric_cols)

pearson_coef, p_value = stats.pearsonr(df['horsepower'], df["price"])
print("The Pearson Coefficient is: ", pearson_coef)
print("The p-value is: ", p_value)

correlation_matrix = df[numeric_cols].corr(method="pearson")
print(correlation_matrix)

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, cmap="coolwarm", annot=True, fmt=".2f", square=True)

plt.title("Pearson Correlation Heatmap")
plt.tight_layout()
plt.show()
