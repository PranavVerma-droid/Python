name = str(input("Please Enter Name: "))
age = int(input("Please Enter Your Age: "))
income = int(input("Please Enter your Taxable Income: "))

def tax_income_calc (a):
    if (a <= 500000):
        print("No Income Tax.")
    elif (a > 500000 and a <= 750000):
        print(str((a - 500000) * 0.1))
    elif (a > 750000 and a <= 1000000):
        print(str((a - 750000) * 0.2))
    else:
        print(str(((a - 1000000) * 0.3) + 9000))

if (age > 60 or age < 18):
    print("Wrong Category.")
else:
    tax_income_calc(income)
    print("Tax Payer Name: " + name)
    
