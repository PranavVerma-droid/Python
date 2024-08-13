string = str(input("Please Enter String: "))
split_string = string.split()

count_1 = 0
count_2 = 0


for i in string:
    if i.isalpha():
        count_1 = count_1 + 1
    else:
        continue
for j in split_string:
    count_2 = count_2 + 1

print("Number of Letters: " + str(count_1))
print("Number of Words: " + str(count_2))

    
