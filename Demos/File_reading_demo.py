# File manipulation demo

import os #imports the OS module
print(os.getcwd()) #prints the path of the working directory

#_____________________________________________Section 1_____________________________________
File1 = open("Demos/Text_folder/Example1.txt", "r")

######Ok way to do it but comes with issues#####
Line_read = File1.readline() #reads the first line of the file
print(Line_read)
Line_read = File1.readline() #reads the second line
print(Line_read)
Line_read = File1.readline() #reads the third line
print(Line_read)
print("\n \n \n")

File1.close() #it is important to close the file to save computational resourses

#_____________________________________________Section 2_____________________________________

#opens the file "file_read_example.txt" from current working directory
#better way is by using a loop & indentation block that automatically closes the file
with open("Demos/Text_folder/Example1.txt", "r") as File1:
    for line in File1:
        print(line)
    print('\n\n\n')
    print("Printing the file name: ", File1.name) # you can also print attributes of the file
    print("Printing the file mode: ", File1.mode) # mode example
    print("Is the file closed while indented with the loop: ", File1.closed)
print("Is the file closed after ending the loop: ", File1.closed)
print('\n\n\n')


#_____________________________________________Section 3_____________________________________

#This example opens the file "Example" saves it as a temp variable "File1"
#Then it uses the read() method to read the entire file and save it to a variable, the prints
with open("Demos/Text_folder/Example1.txt", "r") as File1:
    File_content = File1.read() #this reads the entire file line by line and saves it to a variable
    print(File_content)

#_____________________________________________Section 4_____________________________________
#Basic example of how to write to a file in a line
with open("Demos/Text_folder/Example2.txt", "w") as File2:
    File2.write("This is line A -> writing to file example \n")
    File2.write("This is line B\n")

#_____________________________________________Section 5_____________________________________
#This example creates a list and saves the list item by item to an Example3.txt file using a for loop
Lines_to_write = ["This is lineA\n","This is line B\n", "This is line C\n"]

with open("Demos/Text_folder/Example3.txt", "w") as File3:
    for line in Lines_to_write:
        File3.write(line)

#_____________________________________________Section 6_____________________________________
# This example reads the number of lines in a text file, saves to a variable "line_count" and writes the next line as line_count + 1
def append_next_line_number(file_path):
    # First, count existing lines
    with open(file_path, "r") as f:
        line_count = sum(1 for _ in f)


    with open(file_path, "a") as f:
        f.write(f"This is line {line_count + 1}\n")


append_next_line_number("Demos/Text_folder/Example4.txt")

#_____________________________________________Section 7_____________________________________
# This example show how to copy a file using Python using a for loop

with open("Demos/Text_folder/Example1.txt", "r") as readfile:
    with open("Demos/Text_folder/Example5.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)