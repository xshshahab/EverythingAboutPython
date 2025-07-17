# Using os modules to print all the directory on terminal
import os 

# specify the directory you want to list
directory_path = "/home/username/Videos" # if you're using linux 

# list all the files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name
for eachfile in contents: 
    print(contents)
