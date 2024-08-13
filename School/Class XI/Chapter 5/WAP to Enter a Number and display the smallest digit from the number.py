number = int(input("Please Enter a Number: "))
lastDigit = 9
x = 0


while(number > 0):
    digit = number % 10
    number = number // 10
    if (digit < lastDigit):
        #x = digit
        lastDigit = digit
print(lastDigit)
    
    
