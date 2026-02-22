import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import skillsnetwork
from sklearn.linear_model import LinearRegression
import seaborn as sns

from colorama import init, Fore, Back, Style
init(autoreset=True)


file_path = "Demos/Excel_folder/automobileEDA.csv"
df = pd.read_csv(file_path, header= 0)

print("This prints the top 5 rows of the data in our csv file: ")
print("\n")

# Ensure price is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['curb-weight'] = pd.to_numeric(df['curb-weight'], errors='coerce')
df['peak-rpm'] = pd.to_numeric(df['peak-rpm'], errors='coerce')
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df['engine-size'] = pd.to_numeric(df['engine-size'], errors='coerce')
df['highway-mpg'] = pd.to_numeric(df['highway-mpg'], errors='coerce')
df = df.dropna(subset=['price', 'engine-size', 'highway-mpg'])

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.show()

plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
plt.show()

print(df[['peak-rpm', 'highway-mpg', 'price']].corr())

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(x=df['highway-mpg'],y=df['price'])
plt.show()