# CH4 - This project shows how to use 2D lists as well as how to manipulate them
## Code by NOVA_TAGO
## Gradebook lists projects
## Goal: Learn how to use/manipulate lists


last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]


subjects = ["physics", "calculus", "poetry", "history"]

grades = [98,97,85,88]

#Creates 2D list with both subjects & grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Adds an entry at the end called "computer science"
gradebook.append(["computer science"])

# Adds a value for a grade in the last list
gradebook[-1].append(100)
#print(gradebook) --> dont want to print anymore

# Adds a new course at the end of the list
gradebook.append(["visual arts"])
# Adds a new grade for the new class at the end of the list
gradebook[-1].append(93)

# Changes the last grade in the list to 98
gradebook[-1][-1] = 98

# Removes a value "85" in the third item 
gradebook[2].remove(85)

#Adds a value of "Pass" to the third item
gradebook[2].append("Pass")

#print(gradebook) --> dont want to print anymore

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)