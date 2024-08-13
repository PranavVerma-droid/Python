num1 = int(input("Please Enter Number 1: "))
num2 = int(input("Please Enter Number 2: "))
operator = str(input("Please Enter Operator (+, -, *, /): "))

if (operator == "+"):
    print(num1 + num2)
elif (operator == "-"):
    print(num1 - num2)
elif (operator == "*"):
    print(num1 * num2)
elif (operator == "X" or operator == "x"):
    print(num1 * num2)
elif (operator == "/"):
    print(num1 / num2)
