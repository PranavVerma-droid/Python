currentNumber = 2
prevNumber = 1

totalSum = 0

for i in range(1, 20):
    totalSum = totalSum + (prevNumber * currentNumber)
    prevNumber = currentNumber
    currentNumber = currentNumber + 1
print(totalSum)
