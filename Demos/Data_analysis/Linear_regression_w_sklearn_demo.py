# Demo

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import skillsnetwork
from sklearn.linear_model import LinearRegression

from colorama import init, Fore, Back, Style
init(autoreset=True)


file_path = "Demos/Excel_folder/automobileEDA.csv"
df = pd.read_csv(file_path, header= 0)

print("This prints the top 5 rows of the data in our csv file: ")
print(df.head())
print("\n")

# Ensure price is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['curb-weight'] = pd.to_numeric(df['curb-weight'], errors='coerce')
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df['engine-size'] = pd.to_numeric(df['engine-size'], errors='coerce')
df['highway-mpg'] = pd.to_numeric(df['highway-mpg'], errors='coerce')
df = df.dropna(subset=['price', 'engine-size', 'highway-mpg'])

#____________________Section 1___________________________
print(Fore.GREEN + Style.BRIGHT + "===Intro Section===")  
print("\n")
lm = LinearRegression()

X1 = df[['highway-mpg']]
Y1 = df['price']
lm.fit(X1,Y1)
Yhat=lm.predict(X1)              #Yhat = a + bX
print("This command predicts values for Y at values of X(0-5): ", Yhat[0:5])
print("This command finds the Y intercept: ", lm.intercept_)
print("This command finds the slope of the fit: ", lm.coef_)

plt.scatter(df['highway-mpg'], df['price'], color = 'blue', label='Actual price')
Price_pred = lm.predict(df[['highway-mpg']])
plt.plot(df['highway-mpg'], Price_pred, color = 'red', linewidth=2, label='Regression line')

plt.xlabel('highway-mpg')
plt.ylabel('Price')
plt.title('Linear Regression: Price vs Highway-mpg')
plt.legend()
plt.show()

#____________________Section 1___________________________
lm1 = LinearRegression()
Z = df[['engine-size', 'highway-mpg']]
lm1.fit(Z, df['price'])
##
# Create meshgrid
x_surf, y_surf = np.meshgrid(
    np.linspace(df['engine-size'].min(), df['engine-size'].max(), 30),
    np.linspace(df['highway-mpg'].min(), df['highway-mpg'].max(), 30)
)

grid_df = pd.DataFrame({
    'engine-size': x_surf.ravel(),
    'highway-mpg': y_surf.ravel()
})

fittedY = lm1.predict(grid_df)

# Reshape back to surface format
z_surf = fittedY.reshape(x_surf.shape)

##
lm1_intercept = lm1.intercept_
lm1_slope = lm1.coef_
print("LM1 slope is: ", lm1_slope)
print("Lm1 intercepts are: ", lm1_intercept)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter points
ax.scatter(df['engine-size'], df['highway-mpg'], df['price'], color='blue')

# Regression plane
ax.plot_surface(x_surf, y_surf, z_surf, alpha=0.3)

ax.set_xlabel('Engine Size')
ax.set_ylabel('Highway MPG')
ax.set_zlabel('Price')

plt.show()

