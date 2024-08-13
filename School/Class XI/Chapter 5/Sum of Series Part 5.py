a = int(input("Please Enter Numerator (a): "))
n = int(input("Please Enter n For Formula (2n - 1): "))
totalSum = 0

for i in range(1, 2 * n, 2):
    totalSum = totalSum + (a / i)
print(totalSum)
