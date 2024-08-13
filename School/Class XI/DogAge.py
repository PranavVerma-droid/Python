dogAge = eval(input("Please Enter Dog's Age in Human Years: "))
finalAge = 0
threshold = 21


if (dogAge >= threshold):
    finalAge = finalAge + 2
    finalAge = finalAge + ((dogAge - threshold) // 4)
    print(str(finalAge) + " Years")
elif (dogAge >= (threshold / 2) and dogAge < threshold):
    finalAge = finalAge + 1
    print(str(finalAge) + " Years")
else:
    print("0 Years")
    

