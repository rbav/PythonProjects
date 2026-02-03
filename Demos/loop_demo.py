# Loop_demo

# The following code is a demo for using loops

range_var = range(5) #creates a range starting at 0 and moving 5 places -> 0,1,2,3,4
print(range_var)
for num in range_var:
    print(num, end=" ")

print('\n')
range_var = range(10,15) #creates a range starting at 10 and ending before 15
print(range_var)
for num in range_var:
    print(num, end=" ")

print('\n')
range_var = range(10,20,2) #creates a range starting at 10 and ending before 20 at intervals of 2
print(range_var)
for num in range_var:
    print(num, end=" ")

print('\n')
#standard for loop demo
list_loop_demo_a = [1, 2, 3, 4, 5] #creates a list
sum_loop_selected = 0 #initializes sum variable to 0
index_1 = 1 #variables can be used in range function but have an offset of 1
index_2 = 4
index_num = index_1 - 1
for item in range(index_1 , index_2):
    print("The value at index", index_num, "is", item)
    index_num += 1
    sum_loop_selected += item
print("The sum of values at index", index_1, "to", index_2, "is" , sum_loop_selected)

print('\n')
#another for loop demo
list_loop_demo_b = ['a','b','c','d'] #creates a list with letters a-d
for i, value in enumerate(list_loop_demo_b): #using enumerate gives both the index and the value in the loop
    list_loop_demo_b[i] = "the letter is: " + value #updates the values in the list to include "the letter is: "
print(list_loop_demo_b) #prints out the value to show the loop worked

#standard while loop demo
counter = 0 #initializes the variable at a set value
while counter <= 5: #does the following task as long as the counter is less than 5 -> stops if couner is equal to or greater than 5
    print(counter, end="   |   ") # uses the print command and | symbol to separate values
    counter += 1

print("\n")
#another example but with using lists
color_list = ["orange", "orange", "orange", "blue", "green", "purple", "orange"] #list of colors
new_color_list = [] #empty list
i = 0 #sets i variable to zero again
while(color_list[i] == "orange"): #while loop that adds colors to new_color_list while they are "orange" in old list
    new_color_list.append(color_list[i])
    i += 1
print(new_color_list)

print("\n")
# example with break and continue
count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  # skip printing 3
    if count == 8:
        break     # stop the loop when count is 8
    print(count)