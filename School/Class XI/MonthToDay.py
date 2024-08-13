days30 = ["April", "april", "June", "june", "September", "september", "November", "november"]
days31 = ["January","january", "March", "march", "May", "may", "July", "july", "August", "august", "October", "october","December", "december"] 
days28 = ["February", "february"]

inputMonth = str(input("Please Enter Name of Month: "))

if (inputMonth in days30):
    print("This Month has 30 Days.")
elif(inputMonth in days31):
    print("This Month has 31 Days.")
elif(inputMonth in days28):
    print("This Month has 28/29 Days.")
else:
    print("Please Input a Vaild Month Name.")
