import numpy as np
import math

Point_1 = np.array([0,0,5])                                                 # creates vector 1 as a list
Point_2 = np.array([1,0,3])                                                 # creates vector 2 as a list

v = Point_2 - Point_1
d = np.linalg.norm(v)                                                       # 
d2 = np.sqrt(v @ v)                                                         # Another method
d3 = np.sqrt(np.dot(v, v))

print("The vector between P1 and P2 is:", v)
print("The distance between P1 and P2 is:", d)
print(d2)
print(d3)
