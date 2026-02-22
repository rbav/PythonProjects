#Example of simple 
#__________________________Intro____________________
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

# Initialize constants
A = 1
B = 5       #Shifts parabola left & right
C = 1       #Shifts parabola up and down
D = 2
E = 1

#Generate independent variable X as points on a line between -10 & 10 (200 points included)
X = np.linspace(-10, 10, 200)
#__________________________Linear____________________
Y_linear = (A*X) + B
df = pd.DataFrame({'X': X, 'Y' : Y_linear})

plt.figure()
plt.plot(df['X'], df['Y'])
plt.title('Linear: Y = AX + B')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#__________________________Parabola using Simple Quadratic_______________________


Y = ((A * (X**2)) + (B * X) + C)         # Parenthases not explicitly required, just good practice
df = pd.DataFrame({'X': X, 'Y' : Y})

plt.figure()
plt.plot(df['X'], df['Y'])
plt.title('Quadratic Function: Y = AX^2 + BX + C')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#Find the Vertex
VertX = -B/(2*A)
VertY = (VertX*2) + (B*VertX) + C
print("Vertex occurs at: ", VertX, ":", VertY)


#__________________________Parabola using Polynomial Features_______________________
# Reshape X for sklearn
X_reshaped = X.reshape(-1, 1)

# Generate polynomial features
poly = PolynomialFeatures(degree=2, include_bias=True)
X_poly = poly.fit_transform(X_reshaped)

# Coefficients: [C, B, A]
coefficients = np.array([C, B, A])

# Compute Y using matrix multiplication
Y_model = X_poly @ coefficients

plt.figure()
plt.plot(X, Y_model)
plt.title('Quadratic via PolynomialFeatures')
plt.grid(True)
plt.show()

#__________________________Cubic using Simple Quadratic_______________________


Y = ((A * (X**3)) + (B * X**2) + (C*X) + D)         # Parenthases not explicitly required, just good practice
df = pd.DataFrame({'X': X, 'Y' : Y})

plt.figure()
plt.plot(df['X'], df['Y'])
plt.title('Cubic Function: Y = AX^3 + BX^2 + CX + D')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#__________________________Quartic using Simple Quadratic_______________________


Y = ((A * (X**4)) + (B * X**3) + (C*X**2) + (D*X) + E)         # Parenthases not explicitly required, just good practice
df = pd.DataFrame({'X': X, 'Y' : Y})

plt.figure()
plt.plot(df['X'], df['Y'])
plt.title('Quartic Function: Y = AX^4 + BX^3 + CX^2 + DX + E')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#__________________________Quintic using Simple Quadratic_______________________


Y = ((A * (X**5)) + (B * X**4) + (C*X**3) + (D*X**2) + (E*X) + 1)         # Parenthases not explicitly required, just good practice
df = pd.DataFrame({'X': X, 'Y' : Y})

plt.figure()
plt.plot(df['X'], df['Y'])
plt.title('Quintic Function: Y = AX^5 + BX^4 + CX^3 + DX^2 + EX + F')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#__________________________Sextic using Simple Quadratic_______________________

Y = ((A * (X**6)) + (B * X**5) + (C*X**4) + (D*X**3) + (E*X**2) + X + 1)         # Parenthases not explicitly required, just good practice
df = pd.DataFrame({'X': X, 'Y' : Y})

plt.figure()
plt.plot(df['X'], df['Y'])
plt.title('Sextic Function: Y = AX^6 + BX^5 + CX^4 + DX^3 + EX^2 + + FX + G')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()