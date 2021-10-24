"""File Handling Example 1"""
import os

file = open("C:/Users/Pranav Verma/Desktop/Github/My-Python-Repo/File Opening in Python/Demo.txt")
print(file.read())
file.close()

"""File Handling Example 2"""
import os

file = open("C:/Users/Pranav Verma/Desktop/Github/My-Python-Repo/File Opening in Python/Demo.txt", 'r')
print(file.read())
file.close()

"""File Handling Example 3"""

import os

file = open("C:/Users/Pranav Verma/Desktop/Github/My-Python-Repo/File Opening in Python/Demo.txt", 'r')
print(file.read(6))
file.close()
