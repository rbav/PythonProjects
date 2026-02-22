#Challenge _ Count X

#This time we are going to count the number of occurrences of a certain letter within a string
#code by Nova Tago

#For example "mississippi" has 4 's'

#To do this we will need to perform the following:
#1) Define a function to accept two parameters
    # a word and a character to count
#2) Create a counter to keep track of the number of occurences
#3) Loop through every letter in the string and change the counter if it matches the desired character
#4) Return the counter after the loop

def count_char_x(word, x):
    counter = 0
    for letter in word:
        if letter == x:
            counter += 1
    print(counter)
    return counter


word = input(str("Please enter a word: "))
x = input(str("Please enter a letter to count: "))

count_char_x(word, x)