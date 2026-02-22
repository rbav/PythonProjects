import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

file_path = "Demos/Excel_folder/auto.csv"
df = pd.read_csv(file_path, names = headers)

#set seaborn style for gridelines
sns.set_style("whitegrid")

# Ensure price is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['price'])


sns.boxplot(x='drive-wheels', y='price', data=df, hue = 'drive-wheels', dodge = False, palette=['lightblue', 'lightgreen', 'lightpink'], width  = 0.6)

plt.xlabel('Drive Wheels')
plt.ylabel('Price')
plt.title('Box Plot of Price by Drive Wheels')
plt.grid(True, axis="y", linestyle = "--", alpha = 0.9)
plt.show()


sns.boxplot(x="body-style", y="price", data=df, dodge = False, width  = 0.6)
plt.xlabel('Body-style')
plt.ylabel('Price')
plt.title('Box Plot of Price by body style')
plt.grid(True, axis="y", linestyle = "--", alpha = 0.9)
plt.show()