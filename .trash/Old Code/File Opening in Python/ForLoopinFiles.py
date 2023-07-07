import os
file = open("C:/Users/Pranav Verma/Desktop/Github/My-Python-Repo/File Opening in Python/Demo.txt", 'r')
for line in file:
    print(file.readlines())
file.close()