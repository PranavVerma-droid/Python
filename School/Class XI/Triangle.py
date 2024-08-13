a = int(input("Please Enter Side 1: "))
b = int(input("Please Enter Side 2: "))
c = int(input("Please Enter Side 3: "))

s = (a + b + c) / 2

herons = (s * (s - a) * (s - b) * (s - c)) ** 2

if (herons <= 0):
    print("Not a Triangle")
else:
    if (a == b == c):
        print("Equlateral Triangle.")
    elif (a == b or b == c or a == c):
        print("Isoceles Triangle.")
    else:
        print("Scalene Triangle")
