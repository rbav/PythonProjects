#This project is to display the common methods for operating on strings
#Demo by Nova_Tago

#The capitalize() method 
# Makes first character upper_case if a letter
# Makes all other letters lower_case
print('aBcD'.capitalize())


#The center() method
# Centers the text within a given range using whitespaces
print('[' + 'alpha'.center(10) + ']')


#The endswith() method
#Checks if a string ends with a substring. Returns True if it does and Falst if it doesnt
print("epsilon".endswith("on"))


#The find() method
#Looks through a string for a substring and returns the first occurance
print("MEta".find("ta"))


#The isalnum() method
#looks at a string and checks if it is only composed of letters and numbers
#Returns False if it finds special characters or whitespaces
print('lambda30'.isalnum())


#The isdigit() method
#Looks at a string and checks if it is only composed of numbers
#Returns False if it finds special characters, whitespaces, or letters
print('2018'.isdigit())


#The islower() method
#Looks at a string and checks if it contains capital letters
#returns False if capital letters are found
#does not detect whitespaces or special characters or digits
print('moooo'.islower())


#the isspace() method
#Looks at a string and checks if it contains only spaces
#Returns false if it contains digits or characters
print(" \n".isspace())


#the isupper() method
#looks at a string and checks if it contains only capital letters
#Does not detect special characters, digits, or whitespaces
print(" MOOOO".isupper())


#the join() method
#Takes a list as an argument and joins them together as a single string separated by commas
print(",".join(["omicron", "pi", "rho"]))


#The lower() method
#Makes a new string using a source string but with no capital letters
#converts uppercase letters to lowercase and ignores specail characters, digits, and whitespaces
print("SiGmA=60".lower())


#The lstrip() method
#Removes all leading whitespaces from a string
#Can be modified to remove specific leading characters
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))


#The replace() method
#Looks at a string and replaces all occurances of a substring with another
print("This is it!".replace("is", "are"))


#the rfind() method
#looks at a string for a substring and returns the index, but starts on the right hand side of the string
print("tau tau tau".rfind("ta"))


#The rstrip() method
#Same as the lstrip but it starts on the right side instead
#removes tailing whitespaces
#can be modified to remove specific substrings
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))


#the split() method
#splits a string into a list of all detectable substrings
print("phi       chi\npsi".split())


#the startswith() method
#Looks at a string and checks it if begins with a selected substring
print("omega".startswith("om"))


#the strip() method
#combines the lstrip() and rstrip() methods
print("[" + "   aleph   ".strip() + "]")


#The swapcase() method
# changes all uppercase to lowercase and all lowercase to uppercase
print("I know that I know nothing.".swapcase())


#The title() method
# Changes a string to the Title_case print (Uppercase for the first letter of each word)
print("I know that I know nothing. Part 1.".title())


#The upper() method
# Changes all letters to upper case in a string
print("I know that I know nothing. Part 2.".upper())
