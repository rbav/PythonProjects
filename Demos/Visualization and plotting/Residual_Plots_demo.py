# Residual Plots demo
# Demo for using seaborn to make residual plots to verify if linear fit is good


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_style("darkgrid")

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

file_path = "Demos/Excel_folder/auto.csv"
df = pd.read_csv(file_path, names = headers)

# Ensure price is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['price'])

# Ensure peak-rmp is numeric
df['peak-rpm'] = pd.to_numeric(df['peak-rpm'], errors='coerce')
df = df.dropna(subset=['peak-rpm'])

sns.residplot(x="highway-mpg", y="price", data=df)
plt.show()
print("Although faint, we can see here that the residuals have a curvature")