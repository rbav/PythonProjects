import os

#creates a folder "my_first_directory" in current folder and well as a subfolder "my_second_directory"
#os.makedirs("my_first_directory/my_second_directory")

#changes current directory into "my_first_directory"
#os.chdir("my_first_directory")

#Deletes the directory "my_first_directory"
#os.rmdir("my_first_directory")

#print contents of current directory
print(os.listdir())

#prints working directory
print(os.getcwd())

#creates a directory "my_first_directory" and prints a 0 if it didnt already exist
#returned_value = os.system("mkdir my_first_directory")
#print(returned_value)