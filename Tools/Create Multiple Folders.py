import os
import sys

parent_dir = "C:\\Users\\prana\\Desktop\\A LOT OF FOLDERS"
confirm = input("Are you sure that you want to Continue? ")

if confirm not in "YESyes1":
    print("Exiting.")
    sys.exit(0)

print("Directory Using: " + parent_dir)
dir_number = int(input("Please Enter Number of Directories: "))

if not os.path.exists(parent_dir):
    os.mkdir(parent_dir)
    


for i in range(0, dir_number+1):
    directory = "Folder " + str(i)
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory " + str(i) + " Created.")
