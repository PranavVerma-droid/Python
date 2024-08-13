marks = [0, 0, 0, 0, 0]

i = 0
while(i <= 4):
    marks[i] = float(input("Please enter marks " + str(i + 1) + ": "))
    i = i + 1
average = (marks[0] + marks [1] + marks [2] + marks [3] + marks [4])/5
print(average)
