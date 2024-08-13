x = int(input("Please Enter a 2 digit Number: "))

a = x//10
b = x % 10

if(((a + b) + (a * b)) == x):
    print("The Number is a Special Number")
else:
    print("The Number is a Normal Number.")

