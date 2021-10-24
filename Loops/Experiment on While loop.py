import sys

count = 0
finalcount = int(input("Pls enter the amount of times the loop will repeat: "))

print('When the Count reaches',finalcount,', It will stop.')

while count < finalcount:
    print('Count =', count)
    count = count + 1




print('Count completed.')