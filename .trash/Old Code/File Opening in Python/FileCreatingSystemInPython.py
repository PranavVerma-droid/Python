import os
import sys

#This is a code for creating a file and giving it a function of x in the last
# x = create, a = append, w = write, r = read(default)

#look in the path file. There is no file such as that on the Desktop. So, using the x command(create), we can create a file of that name on the desktop
#and the file contents you can modify using file.write() function.

file = open("C:/Users/Pranav Verma/Desktop/NewFileCreatedInPython.txt", 'x')
file.write("FileContentsGoHere") #After You run this file, this will create a newfile named above with the name given above. give it a try xD
file.close()