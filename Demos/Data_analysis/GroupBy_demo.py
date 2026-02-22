import pandas as pd
import matplotlib.pyplot as plt

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

file_path = "Demos/Data/Excel_folder/auto.csv"
df = pd.read_csv(file_path, names = headers)

df_test = df[['drive-wheels','body-style','price']]     #Takes the 3 listed columns and makes a new dataframe falled df_test 

df_grp = df_test.groupby(['drive-wheels','body-style','price'], as_index=False).mean()  #groups df_test by each variable
print(df_grp.head(50))
print("\n\n")
