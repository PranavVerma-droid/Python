number = int(input("Please Enter Number Here: "))
x = 0

for i in range(2, number):
    if number%i == 0:
        x = 1
        
if (x == 0):
    print("Number is Prime.")
else:
    print("Number is NOT Prime.")
        
    
