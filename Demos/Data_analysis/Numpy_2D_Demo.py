# Numpy Demo - 2D+ Numpy
import numpy as np
from colorama import init, Fore, Back, Style
init(autoreset=True)

#___________________________________________section break_____________________________________________
print("\n")
print(Fore.RED + Style.BRIGHT + "===Intro Section===")  
List_a = [[11,12,13],[21,22,23],[31,32,33]]     # List with lists as elements (Nested list)
Array_a = np.array(List_a)                      # Converts List_a into a 3x3 matrix

print(Array_a)

# rank has to do with how many lists are in the list and not the dimensions of the array
print("The rank of matrix \'Array_a\' is: ", Array_a.ndim)
print("The dimensions of matrix \'Array_a\' is: ", Array_a.shape)
print("The size of \'Array_a\' is: ", Array_a.size)
# Indexing the matrix Array[Row, Coloumn]
print("The value of the second row, second & third columns are: ", Array_a[1,1:3])
print("The value of the second & third rows, first column are: ", Array_a[1:3,0])

#Matrix addition example
Matrix_x = np.array([[1,0],[0,1]])
Matrix_y = np.array([[2,1],[1,2]])
print(Matrix_x)
print(Matrix_y, "\n")
Matrix_z_add = np.add(Matrix_x, Matrix_y)
print("Matrix_x + Matrix_y is: \n", Matrix_z_add)
print("Matrix_z * 3 is: \n", (np.multiply(Matrix_z_add, 3)))

Matrix_a = np.array([[0,1,1],[1,0,1]])                    # 3x2 matrix !!!Number of Col(Matrix_a) must = number of Row(Matrix__b))
print("Matrix_a is: ", Matrix_a)
Matrix_b = np.array([[1,1],[1,1],[-1,1]])                 # 2x3 matrix
print("Matrix_b is: ", Matrix_b)
Matrix_ab = np.dot(Matrix_a, Matrix_b)
print("\n")

A = np.array([[1,2,4,5,6],[3,4,9,8,8]])
B = np.array([[1,2],[4,5],[7,8],[7,8],[7,8]]) 
print(A)
print(B)
C_dot = np.dot(A,B)
print("The dot product between A & B is: ")
print(C_dot)
A_transpose = A.T
print("The Transpose of A is: ")
print(A_transpose)
eye_matrix = np.eye(5)               #builds an identity matrix (row reduced of "n" rows)
print(eye_matrix)
diag_matrix = np.diag(eye_matrix)    #builds a matrix from the diagonal values of another matrix
print(diag_matrix)
print("\n")
stacked_ab = np.hstack(A)
print(stacked_ab)
print("\n\n\n")

print(Fore.RED + Style.BRIGHT + "===DEMO Section===")
