# Your code below:
#Loops review
#Code by NOVA_TAGO

single_digits = range(10)
#creates a number list that ranges from 0-9 (includes 9) 

squares = []
#creates an empty list called squares

for num in single_digits:
#goes through the numbers in single_digits one at a time
  print(num)
  #prints out each iteraction of the for loop on separate lines
  squares.append(num**2)
  #takes each number during the loop and X^2 it then
  #adds it to the list called "squares"

print(squares)
#prints the list "squares" on the same line

cubes = [num**3 for num in single_digits]
#creates a list of the cubes for each number in the list single digits
#this code utilizes the list comprehension methods

print(cubes)
#prints the list "cubes" onto a single line

