string = str(input("Please Enter 3 Word Name: "))
split_string = string.split()
import sys

if len(split_string) == 3:
    in1 = split_string[0][0:1]
    in2 = split_string[1][0:1]
    in3 = split_string[2][0:1]

    print(in1 + in2 + in3)

else:
    print("Please Enter a 3 Word Name.")
    sys.exit()