"""Creating a File First(Select this part and run it first)"""
import os

file = open("C:/Users/Pranav Verma/Desktop/FileDeletionSystem.txt", 'x')
file.write("This is a file to demonstrate the file deletion system in python")
file.close()

"""Deleting a File"""
import os

if os.path.exists("C:/Users/Pranav Verma/Desktop/FileDeletionSystem.txt"):
    os.remove("C:/Users/Pranav Verma/Desktop/FileDeletionSystem.txt")
else:
    print("The File does not exist!")

