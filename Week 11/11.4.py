#filesystem prac!
import sys, os 

#get system platform
print(f"\nCurrent platform is {sys.platform}")

#print current working directory
print(f"Current working directory is {os.getcwd()}")

#create directory, named by user input in cwd
dir_name = input("Name of directory: ")
os.mkdir(dir_name)
print(f"New directory created: {dir_name}")
print("Thanks byeeee!")