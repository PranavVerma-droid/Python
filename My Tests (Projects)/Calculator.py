import sys


# define the variables.
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def power(x, y):
    return x ** y


# start the calculator.
def calculator():
    active = True
    while active:
        print("choose one of the following options:")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. power")
        choice = input("Your Input(in numbers):")
        if choice in ("1", "2", "3", "4","5"):
            num1 = float(input("enter the first number: "))
            num2 = float(input("enter the second number: "))
            if choice == "1":
                print(num1, "+", num2, "=", add(num1, num2))
                ans = input("do you want to use this again (y/n): ")
                if ans == "n":
                    break
            elif choice == "2":
                print(num1, "-", num2, "=", subtract(num1, num2))
                ans = input("do you want to use this again (y/n): ")
                if ans == "n":
                    break
            elif choice == "3":
                print(num1, "*", num2, "=", multiply(num1, num2))
                ans = input("do you want to use this again (y/n): ")
                if ans == "n":
                    break
            # there seems to be a problem here...
            elif choice == "4":
                if num2 == "0":
                    try:
                        print(num1, "/", num2, "=", divide(num1, num2))
                    except ZeroDivisionError:
                        print("you can't divide by zero!")
                else:
                    print(num1, "/", num2, "=", divide(num1, num2))
                ans = input("do you want to use this again (y/n): ")
                if ans == "n":
                    break

            elif choice == "5":
                print(num1, "Raised to the Power of", num2, "=", power(num1,num2)
                ans = input("do you want to use this again (y/n): ")
                if ans == "n":
                    break



            else:
                print("invalid input!")


calculator()