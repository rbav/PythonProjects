#Piplines Demo


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from colorama import init, Fore, Back, Style

init(autoreset=True)

file_path = "Demos/Excel_folder/automobileEDA.csv"
df = pd.read_csv(file_path, header= 0)

# Ensure price is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['curb-weight'] = pd.to_numeric(df['curb-weight'], errors='coerce')
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df['engine-size'] = pd.to_numeric(df['engine-size'], errors='coerce')
df['highway-mpg'] = pd.to_numeric(df['highway-mpg'], errors='coerce')
df = df.dropna(subset=['price', 'engine-size', 'highway-mpg'])

pr = PolynomialFeatures(degree=2)
x = df['highway-mpg']
y = df['price']
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
Z_pr = pr.fit_transform(Z)
print(Z.shape)
print(Z_pr.shape)

Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
pipe = Pipeline(Input)
print(pipe)

Z = Z.astype(float)
pipe.fit(Z,y)

ypipe=pipe.predict(Z)
print(ypipe[0:4])
print("\n\n")

#_______________________________________________________
#Create a pipeline that standardizes the data, then produces a prediciton using linear regression
# Use the features Z and the target Y

Input=[('scale',StandardScaler()),('model',LinearRegression())]

pipe=Pipeline(Input)

pipe.fit(Z,y)

ypipe=pipe.predict(Z)
ypipe[0:10]
print(ypipe)
print("\n")

#________________________Simple Linear Regression
#highway_mpg_fit
lm = LinearRegression()
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X, Y)
# Find the R^2
print('The R-square is: ', lm.score(X, Y))
print('\n')

#________________________
# We can predict output from Yhat using the predict method(X)
Yhat=lm.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])
print('\n')

#________________________
#mean square error
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(df['price'], Yhat)
print('The mean square error of price and predicted value is: ', mse)
print('\n')

#________________________
#multiple linear regression
# fit the model 
lm.fit(Z, df['price'])
# Find the R^2
print('The R-square is: ', lm.score(Z, df['price']))
Y_predict_multifit = lm.predict(Z)
print('The mean square error of price and predicted value using multifit is: ', \
      mean_squared_error(df['price'], Y_predict_multifit))
print('\n')

#________________________
#Polynomial fittings 
from sklearn.metrics import r2_score
x = df['highway-mpg']
y = df['price']
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)
r_squared = r2_score(y, p(x))
print('The R-square value is: ', r_squared)
mean_squared_error(df['price'], p(x))
print('\n')

#______________________________
#prediction and decision making
#Already imported numpy & matplotlib
new_input=np.arange(1, 100, 1).reshape(-1, 1)
lm.fit(X, Y)
lm
yhat=lm.predict(new_input)
print(yhat[0:5])
plt.plot(new_input, yhat)
plt.grid(True)
plt.show()