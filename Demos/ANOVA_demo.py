#ANOVA Demo --> ANalysis Of VAriance (ANOVA)

import pandas as pd
import matplotlib.pyplot as plt
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

# Group by make and calculate average price
avg_price_by_make = df.groupby('make')['price'].mean()
avg_price_by_make = avg_price_by_make.sort_values()

# Plot as a bar chart
plt.figure(figsize=(12, 6))
avg_price_by_make.plot(kind='bar')

plt.xlabel('Make')
plt.ylabel('Average Price')
plt.title('Average Price by Car Make')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

#plt.show()

#the plot above shows relationship between make and price. It looks like jaguars are more expensive than hondas. 
#F tests from ANOVA can see if this can be treated as a variable in price

# F = (Variance between group means)/(Variance within groups)
# A large F value means the group means are far apart compared to the variablility within each group (F ~ 1 is noise)

# p-value is the probability of observing an F-statistic this large if the null hypothesis were true "All group means are equal and there is no relationship"
df_anova = df[['make', 'price']]
grouped_anova = df_anova.groupby(['make'])
anova_results_1 = stats.f_oneway(grouped_anova.get_group(("honda",))["price"], grouped_anova.get_group(("jaguar",))["price"])
print(anova_results_1)

# Overall, if the ANOVA test gives a large F-test value and small p-value
# Then we can say that there is a strong correlation between a caregorical variable and other variables