num = int(input("Please Enter an Positive Even or Negative Odd Number: "))


if (num % 2 == 0 and num > 0):
    print(num, num + 2, num + 4, num + 6)
elif (num == 0):
    print("Number is Neither Odd Or Even.")
elif (num % 2 == 1 and num < 0):
    print(num, num - 2, num - 4, num - 6)
else:
    print("Number is not an Positive Even or Negative Odd Number.")
