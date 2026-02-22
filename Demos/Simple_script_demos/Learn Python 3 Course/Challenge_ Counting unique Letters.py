#Count Letters String Challenge _ CODECADEMY LEARN PYTHON 3 COURSE
#Code by Nova Tago

#We are going to count the number of unique letters in a string
# This means we will need to verify that no duplicates occur
# We should also make all letters the same case before counting

#What we need to do for this challenge
#1) Define the function to accept one parameter - the word
#2) Create a counter to keep track of unique letters
#3) Look through every letter in our alphabet string and increase count for non-duplicates
#4) Return the count after looping through all letters of the word

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(input_word):
    counter = 0
    for letter in letters:
        if letter in input_word:
            counter += 1
    print(counter)



input_word = input(str("Please enter a word for counting: "))
unique_english_letters(input_word)