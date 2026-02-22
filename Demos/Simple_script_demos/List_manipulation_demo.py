#List manipulation demo

# Creates a list named "Numbers_list"
Numbers_list = [5,2,3,4,10,11]

#changes the first value from 1 to 5
Numbers_list[0] = 1 

#deletes the last value from the list
del Numbers_list[-1] 

#adds the value 15 at the end of the list
Numbers_list.append(15) 

print("Displays the first value of the list on the consol \n")
print(Numbers_list[0])
print("\n")

print("Displays the last value of the list on the consol")
print(Numbers_list[-1])
print("\n")

print("Displays all of the values from the list except the last two")
print(Numbers_list[:-2])
print("\n")

print("Displays all the values of the list on the consol except those before the 1 position (second value)")
print(Numbers_list[1:])
print("\n")

print("Displays the values of the list between 2 and 4 (not including position 4)")
print(Numbers_list[2:4])
print("\n")

length = len(Numbers_list)
print("the length of the list is:", length)

# List methods demo

# Creates a list with numbers 0-5 and calls it list_a
list_a = [0,1,2,3,4,5]

# changes the type of element at position "0" in list_a from and integer to a string
# This is called type casting 
list_a[0] = str(list_a[0])
list_a[1] = bool(list_a[1])
list_a[2] = float(list_a[2])

#print list_a to show that the element at position 0 is now a string, position 1 is now a boolean, and position 2 is now a float
print(list_a)
#prints the type for each of the following elements 0, 1, 2, & 3
print(type((list_a[0])), type(list_a[1]), type(list_a[2]), type(list_a[3]))

print("\n")
 
# extend() method is used to add in several new elements, separated by commas
# can add n-dimensional items by putting list inside of a single argument as shown below
list_a.extend([6, 7, [9,[8, 8]]])
print(list_a)

# append() method is used to add in a single new element, here providing multiple arguments makes it an n-dimensional list
# multiple arguments does not add multiple new elements
list_a.append(["9a", "9b"])
print(list_a)

# deletes an item from the list -> element at position 3 will be removed
list_a.pop(3)
print(list_a)

# replaces an item in the list "from position 2" to new value of 7
list_a[2] = (7)
print(list_a)

# deletes the first instance of an argument
list_a.remove(7)
print(list_a)
print("\n")
# .split() method takes a string and turns it into a list while delimiting it using a selectable character
list_b = ("A,B,C,D,E").split(",")
print(list_b)

print("\n")
# shows methods for cloning lists vs copying lists
list_c = list_b[:] #clones list_b to list_c -> any changes on list_c will not occur on list_a
list_d = list_b #copies list_b to list_d -> any changes will occur on both lists
list_d[1] = "BBBBBBB" #changes the list saved to variables list_d & list_b simultaneously
list_c[0] = "AAA"   #changes the list saved to variable list_c only
print("list_b is: " , list_b)
print("list_c is: " , list_c)

print("\n")


#Creates a few sets -> sets use curly brackets and are not ordered like lists or tuples
# uses union command to take all the contents of set _1 and set_2 and saves it to set_3 -> no duplicates allowed
album_set_1 = {"A", "B", "C"}
album_set_2 = {"A", "D"}
album_set_3 = album_set_1.union(album_set_2)
print(album_set_3)

#Checks if album_set_4 is a sub set of album_set_3 -> does album_set_3 contain all of the contents of album_set_4
album_set_4 = {"A", "B", "D"}
print(album_set_4.issubset(album_set_3))

#set manipulation methods (adding and removing)
album_set_4.add("E")
album_set_4.remove("B")
print(album_set_4)

#Converting a list to a set
list_albums = ['rap','house','electronic music', 'rap']
set_from_list = set(list_albums)
print(set_from_list)

#________________________________________Section_________________________________________
# manipulating dictionaries

my_dictionary = {'a':0,'b':1,'c':2, 'd':5}
print(my_dictionary['a'])

print("dictionary keys are: ", my_dictionary.keys())
print("dictionary values are: ", my_dictionary.values())

print("\n")

my_dictionary["e"] = 5 #adds a new key of "e" and sets its value to 5
del(my_dictionary['c']) #deletes the key of "c" and its associated value
print(my_dictionary)
