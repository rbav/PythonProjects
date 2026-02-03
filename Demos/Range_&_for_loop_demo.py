my_list = []  # Creating an empty list.
my_list2 = []

#Inserts values into my_list as long as the range and places the value of that position in reverse order
for i in range(14):
    my_list.insert(0, i)

#Makes additions to my_list2 with the values of i ranging from 0 to 13
for i in range(14):
    my_list2.append(i)

print(my_list)
print(my_list2)

#_________________________________________________________-Section 2-______________________________________

#makes an empty list
my_list3 = [10, 1, 8, 3, 5]
#initializes a variable to zero
total = 0

#counts the length of the list, makes it into a range for a for loop
for i in range(len(my_list3)):
    #adds the value at the selected indice within the list to the variable total
    #In other words, this for loop sums up the value of all entries within a list
    total += my_list3[i]

print(total)
