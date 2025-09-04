#Q.Write a python program to print the contents of a directory using the os module
import os
#specify the directory that you want to list
directory_path =  '/'
#List all files & directories in the specified path
contents= os.listdir(directory_path)
#Print each file & directory name 
for item in contents:

    print(item)
