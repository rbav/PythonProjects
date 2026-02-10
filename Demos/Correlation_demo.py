#Correlation demo

#Examples 
    # Lung Cancer -> Smoking
    # Rain -> Umbrella

# Important to know that correlation doesnt imply causation
    # For example, with correlation, we cant say if the rain caused the umbrella or if the umbrella caused the rain


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


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

sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.show()

#This plots the data as points in a scatterplot format
#Then plots the least-squares linear regression line "Line of best fit"
        # y = B0 + B1x      where x = engine size, y = predicted price, B0 = intercept, B1 = slope
        # This line gives you the average predicted price for a given engine size
# The light blue shaded regions around the dark blue lines is the confidence intervals OF THE AVERAGE PRICE *not the data points 
    # (default of 95% around the regression line)
    # We are ~95% confident that the true population regression line lies within this band
    # Widens at the edges b/c there are fewer data points at extreme values and the model is less certain there


sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.show()
# This plot shows that the better the highway-mpg, the lower the price. The negative slope shows a negative correlation

sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
plt.show()
# This plot shows a weak correlation