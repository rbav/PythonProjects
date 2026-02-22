# Numpy Demo - 1D Numpy
#Numpy is a python library for scientific computing

#___________________________________Section 1______________________________________
#How to create a Numpy array

import numpy as np
import math
import sympy as sp

from colorama import init, Fore, Back, Style

# Initialize colorama (required for Windows/VSCode)
init(autoreset=True)                                            # makes styles only for that string without changing others

#___________________________________________section break_____________________________________________

list_a = ['0',1,'two','3',4]                                    # creating a list to compare to numpy array
list_b = [0,1,2,3,4]                                            # numpy arrays or "ndarray" usually are made of elements of the same type
array_a = np.array(list_b)                                      # casting the list as an array using numpy

#___________________________________________section break_____________________________________________
#Getting information about a formed array
print("\n")
print(Fore.RED + Style.BRIGHT + "===Intro Section===")         # method of changing printed statments appearance for easy display
print(array_a)                                                  # Displays the ndarray
print(type(array_a))                                            # Displays the data type 
print(array_a.dtype)                                            # Displays the data type of the arrays elements (int = integer, Bool = boolean, etc)
print(array_a.size)                                             # Displays the size of the array
print(array_a.ndim)                                             # Displays the number of dimensions of the array
print(array_a.shape)                                            # Displays a tupple of integers indicating the size of the array in each dimension
array_b = array_a[0:3]                                          # Example of slicing and copying an array
print("Array B is : ", array_b)
array_a[3:5] = 300 ,400                                         # can assign new values at specific slices
print("numpy version is: ", np.__version__) 
array_np = np.array([0,1,2,3,4,5,6])                            # method of creating an Numpy array with a list
print(array_np)
array_zeros = np.zeros(6)                                       # method of creating a NumPy array with () digits of zeros
print(array_zeros)
array_ones = np.ones(5)                                         # method of creating a NumPy array with () digits of ones
print(array_ones)

#___________________________________________section break_____________________________________________
#Vector math section 
print("\n")
print(Fore.BLUE + Style.BRIGHT + "===Vector Math Section===")
# coded example using procedural python w/o NumPy
# make vectors into list
vector_u = [1,1]                                                # creates vector u as a list
vector_v = [1,0]                                                # creates vector v as a list
vector_z = []                                                   # creates empty list z
for n,m in zip(vector_u,vector_v):                              # for loop that zips u & y into a 2D list
    vector_z.append(n+m)                                        # adds the element to form z = u + v
print(vector_z)

# coded example using NumPy                                     # Runs faster than above code (important for large datasets)
vector_a = np.array([1,1])                                      # creates vector a as a list
vector_b = np.array([1,0])                                      # creates vector b as a list
vector_c = vector_a + vector_b
print(vector_c)

# coded example of distance calc using NumPy                              
Point_1 = np.array([0,0,5])                                                # creates vector 1 as a list
Point_2 = np.array([1,0,3])                                                # creates vector 2 as a list

vector_P12 = Point_2 - Point_1
distance_12 = np.sqrt(np.sum((Point_2 - Point_1)**2))

print("The vector between P1 and P2 is: ", vector_P12)
print("The distance between P1 and P2 is: ", distance_12)

# coded example of distance calc between two points using python without NumPy                              
P1 = [0,0,5]
P2 = [1,0,3]

differenceP_12 = []
for n,m in zip(P1,P2):
    differenceP_12.append(m-n)
print("The vector_12 between P1 and P2 is: ", differenceP_12)
squares_sum = 0
for component in differenceP_12:
    squares_sum += component ** 2
magnitude_scalar_P12 = math.sqrt(squares_sum)
print(magnitude_scalar_P12)
print("\n")

#___________________________________________section break_____________________________________________
# Arithmatic examples section
print(Fore.GREEN + Style.BRIGHT + "===Arithmatic Section===")
# addition
uu = np.array([1,2,3,-1])
zz_add = uu + 1                                     #This propery is known as broadcasting
print("uu array: ", uu, "plus 1 is: ", zz_add)

#subtraction
zz_minus = uu - 3
print("uu minus 3 is: ", zz_minus)
zz_minus_2 = np.subtract(uu, zz_minus)
print("Numpy subtract method ", zz_minus_2)

# multiplication 
Vector_AA = np.array([1,2,3])
Vector_BB = np.multiply(Vector_AA, 2)
print("Vector_AA * 2 is", Vector_BB)

#division
zz_division = uu / 3.0
print("uu divided by 3 is: ", zz_division)

# power(a,b)
zz_power = np.power(uu, 3)
print("uu to the power of 3 is: ", zz_power)

# remainder
zz_mod = np.mod(uu, 3)
print("uu remainder when 3 is used is: ", zz_mod)

#exponentials (exp(X))
zz_exp = np.exp(uu)
print("exponentials: ", zz_exp)

zz_log = np.log(uu)
print("log of uu is: ", zz_log)

zz_log10 = np.log10(uu)
print("log base10 of uu is: ", zz_log10)

zz_sqrt = np.sqrt(uu)
print("The square root of uu is: ", zz_sqrt)

zz_square = np.square(uu)
print("The square of uu is: ", zz_square)

# Hadamard product (Product of two numpy arrays)
uu = np.array([1,2])
vv = np.array([3,2])
zz_hadamard = uu*vv
print("The Hadamard product of np.array uu: ", uu, "and np.array vv: ", vv, "is:")
print(zz_hadamard)
zz_dot = np.dot(uu, vv)
print("The dot product of np.array uu and vv is: ", zz_dot)

#___________________________________________section break_____________________________________________
print("\n")
print(Back.GREEN + Fore.BLACK + Style.BRIGHT + "===Rounding & Logic Section===")
#Demo of Numpy rounding functions
Array_Floats = np.array([0.15, 0.22, -1.55, 5.44, -4.33, 8.97, 0.22, 0.22, 0.22])   #NumPy method for making an array with () values
print(Array_Floats)
Array_absolute_values = np.abs(Array_Floats)                                        #NumPy method for getting absolulte values 
print("The absolute values of \'Array Floats\' is: ", Array_absolute_values)
Array_rounded = np.round(Array_Floats)                                              #NumPy method for rounding to nearest whole number
print("Rounded version of \'Array_Floats\' is: ", Array_rounded)
Array_floor = np.floor(Array_Floats)                                                #Numpy method for rounding down to nearest whole number
print("Numpy floor rounding method results: ", Array_floor)
Array_ceiling = np.ceil(Array_Floats)                                               #Numpy method for rounding up to the nearest whole number
print("Numpy ceiling rounding method results: ", Array_ceiling)
Array_sign = np.sign(Array_Floats)                                                  #Numpy method for finding the signs of each number
print("Numpy method for sign of values: ", Array_sign)
Array_is_equal = np.equal(Array_Floats, 0.22)                                       #Numpy method for equality check-> returns booleans
print("Numpy method of equality check on Arrays to set value", Array_is_equal)
Array_is_not_equal = np.not_equal(Array_Floats, 0.22)                               #Numpy method for inequality check
print("Numpy method of inequality check with set value")
Array_is_greather_than = np.greater(Array_Floats, 1.00)                             #Numpy method for checking if a numpber is greater than
print("Numpy method for checking if a number is greater than another: ", Array_is_greather_than)
Array_is_less_than = np.less(Array_Floats, 1.00)                                    #Numpy method for checking if a numpber is less than
print("Numpy method for checking if a number is less than another: ", Array_is_less_than)
Array_clipped = np.clip(Array_Floats, 0,5)                                          #Numpy method of limiting values (Any value outside range is set to limiter)
print("The clipped values of Array_Floats between 0 & 5:", Array_clipped)
Array_where = np.where(Array_Floats > 0, Array_Floats, 0 )                          #Numpy method of checking where a condition is true (Replaces values with X when true Y when False)
print("Array_where when more than 0 is:", Array_where)                              #This is a really nice method to remove any values outside of a region for later math operations

Array_sorted = np.sort(Array_Floats)                                                #Numpy method for sorting the values of an array
print("The sorted verison of Array_Floats is:", Array_sorted)                       
Array_argsorted = np.argsort(Array_Floats)                                          #Numpy method for returning the indecies that would sort the array instead of their actual values
print("The argsorted version of Array_Floats is: ", Array_argsorted)
Array_unique = np.unique(Array_Floats)                                              #Numpy method for finding the unique values for an array
print("The unique values of \'Array_Floats\' is: ", Array_unique)

a_logical = True                                                                    #Creating boolean values
b_logical = False
Check_logical_and = np.logical_and(a_logical, b_logical)                            #Numpy method for and logical check
print(Check_logical_and)
Check_logical_or = np.logical_or(a_logical, b_logical)
print(Check_logical_or)

#___________________________________________section break_____________________________________________
print("\n")
print(Fore.CYAN + Style.BRIGHT + "===Statistics Section===")
#Demo of simple Numpy functions
aaa = np.array([1,2,3,4,5])

#Statistics section
mean_aaa = np.mean(aaa)                                             # Can get the mean of an array using mean ()
print("the mean of aaa array is: ", mean_aaa)             
median_aaa = np.median(aaa)                                         # can get the median with np.median()
print("the median of aaa array is: ", median_aaa)
standard_deviation_aaa = np.std(aaa)                                # can get the standard deviation with np.std()
print("the standard deviation of aaa array is: ", standard_deviation_aaa)
variance_aaa = np.var(aaa)                                          # Can get the variance usince np.var()
print("The variance of aaa is: " , variance_aaa)
max_aaa = np.max(aaa)                                               # can get the maximum of an array using np.max()
print("the max of aaa array is: ", max_aaa)
min_aaa = np.min(aaa)                                               # Can get the mimimum of an np array using np.min()
print("The minimum of aaa is: ", min_aaa)
sum_aaa = np.sum(aaa)                                               # can get the sum of aaa array using np.sum(aaa)
print("the sum of aaa is: ", sum_aaa)
cummulative_sum_aaa = np.cumsum(aaa)                                # shows the history of the sum function at each step
print("The cummulative sum of aaa is: ", cummulative_sum_aaa)       
print("\n")


#___________________________________________section break_____________________________________________
print(Fore.MAGENTA + Style.BRIGHT + "===Trigonometry Section===")
# Trigonometry section & functions 

print("using NumPy the value of pi is: ", np.pi)                # how to get value of pi using numpy
x = np.array([0, np.pi/2, np.pi])                               # creates an array of 0, pi/2, and pi
y = np.sin(x)
print(y)                                                        
print("rounding error causes sin(pi) to be 1.2e-16 not 0")

#also have 
    # np.sin(x) for sine
    # np.cos(x) for cosine
    # np.tan(x) for tangent
    # np.arcsin(x) for inverse sine
    # np.arccos(x) for inverse cosine
    # np.arctan(x) for inverse tangent

Degrees_a = 180
radians_a = np.deg2rad(Degrees_a)
print("180* to radians is: ", radians_a)
radians_b = np.pi
Degrees_b = np.rad2deg(radians_b)
print("pi radians to degrees is: ", Degrees_b)

#below is the fix for rounding error (Use sp not np) s=symbolic n=numerical
print("using SymPy, sin of pi is:", sp.sin(sp.pi))                                            # This works because sympy does symbolic math and not numerical


#___________________________________________section break_____________________________________________
print("\n")
print(Fore.YELLOW + Style.BRIGHT + "===Linespace & range Section===")

range_a = np.arange(-4,2,0.5)                                   # Numpy method for creating a range (start at, stop before, interval)
print(range_a)
linea = np.linspace(-2,2,5)                                     #Numpy version of range generator *start, end, number of points)
print(linea)
lineb = np.linspace(-2,2,9)
print(lineb)

import matplotlib.pyplot as plt                                 # imports the visualization modules

x2 = np.linspace(0, 2*np.pi, 50)                                # creates a range between 0,2pi with 50 points
y2 = np.sin(x2)                                                 # solves for sin(x2) from above line at each point

plt.plot(x2,y2, linestyle = 'None', marker = 'o')               # plots each point X2 & Y2, uses linestyle to plot points not lines
plt.xlabel("Input Range")                                       # configures x-axis label
plt.ylabel("Amplitude")                                         # configures y-axis label
plt.show()                                                      # Generates the actual plot in a pop up