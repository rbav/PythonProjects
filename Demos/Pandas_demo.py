# Example of using Pandas, a popular library for data analysis
# Useful for data analysis & data wrangling 

import pandas as pd# gains access to a large number of pre-build classes & functions
import datetime
from colorama import init, Fore, Back, Style
init(autoreset=True)

pd.set_option("display.colheader_justify", "left")
pd.set_option("display.max_colwidth", 20)

#process to convert from csv file to dataframe
xlsx_path = 'Demos/Excel_folder/GC_excel_demo.xls'          # saves file location as a variable
df = pd.read_excel(xlsx_path, sheet_name = "Results")       # uses variable as an argument & saves to variable df #sheet_name allows you to define which sheet in excel

print("\n\n Printing df.info \n")
print(df.info)                                              # prints first and last 5 lines and structure & data types
print("\n\n Printing df.columns \n")
print(df.columns)                                           # prints summary statistics
print("\n\n Printing df.index \n\n")
print(df.index)                                             # Prints the info on the number of lines in the file
print("\n\n Printing df.isna \n\n")
print(df.isna())                                            # prints information on detected missing values
print("\n\n Printing df.fillna \n\n")
print(df.fillna(0))                                         # prints first and last 5 lines -> missing values are replaced with (0)

print("\n\n Printing df.head(50) \n")
print(df.head(50))                                         # can use the method head() to observe the first few lines (default = 5?) -> can select number by inserting into ()
print("\n\n\n Printing df.tail(15) with formatting \n")
print(df.tail(15).to_string(col_space=20, index=True))     # same as above but with some formatting: col_space -> makes things certain width, index = True -> Gives line number (starts at 0)
print("\n\n")

#Example of casting to dataframe
print("You can also use data frames on dictionaries by casting them \n")
songs = {'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat out of hell'], 'Released': [1982,1980,1973,1992,1977], 'Length':['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33']}
songs_frame = pd.DataFrame(songs)
print(songs_frame.head(10))

# checks the column "Released" from dataframe "songs_frame" for how many unique items there are and forms a list
print(songs_frame['Released'].unique())                     # 

#example of finding information for specific places
print(songs_frame.iloc[3,1])                                # (row_index, column_index)
print(songs_frame.iloc[0:2,0:3])                            # can also perform slicing as shown with this print command
print('\n\n')

#example of how to make a new df of specific data
songs_frame2 = songs_frame[songs_frame['Released']>=1980]
print(songs_frame2)

#how to save to dataframe "songs_frame2 as a csv file
songs_frame2. to_csv('Demos/Text_folder/new_songs.csv')

print("\n\n")
print(Fore.BLUE + Style.BRIGHT + "========= Data Wrangling Demo =========")
print("\n")

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

file_path = "Demos/Excel_folder/auto.csv"
df = pd.read_csv(file_path, names = headers)

print(df.head(50))
description = df.describe()                                     # Gives some statistics on the values that show up in the chart
print(description)
print("\n\n")
description2 = df["drive-wheels"].value_counts()                # Reads the drive-wheels column and counts how many of each type show up
print(description2)