prevNumber = 2
currentNumber = 4

totalSum = 0

flag = 0

while (flag >= -20):
    totalSum = totalSum + (prevNumber - currentNumber)
    prevNumber = currentNumber + 2
    currentNumber = currentNumber + 4
    flag = -currentNumber

print(totalSum)
