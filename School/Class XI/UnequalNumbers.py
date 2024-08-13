num1 = int(input("Please Enter Number 1: "))
num2 = int(input("Please Enter Number 2: "))
num3 = int(input("Please Enter Number 3: "))

array = [num1, num2, num3]

if (num1 == num2 or num2 == num3 or num1 == num3):
    print("Please Enter Unequal Numbers.")
else:
    array.sort()
    print(array[1])
    
    
