number = int(input("Please Enter Number: "))

if(number % 2 == 0):
    number = number + 1

for i in range(number, number + 20, 2):
    print(i)
