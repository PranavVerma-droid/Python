num1 = int(input("Please Enter Number 1: "))
num2 = int(input("Please Enter Number 2: "))

if (num1 == num2):
    print("Numbers are equal.")
elif (num1 < num2):
    print(str(num1 ** 2), str(num2 ** 3))
else:
    print(str(num1 ** 3), str(num2 ** 2))
    
