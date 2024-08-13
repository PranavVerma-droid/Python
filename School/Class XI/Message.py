name = str(input("Please Enter Name: "))
age = int(input("Please Enter Age: "))
ageToHundred = int(100 - age)
willwere = ""

if(ageToHundred < 0):
    willwere = "were"
else:
    willwere = "shall be"

print("There is a Message for you:")
print(name + ", You " + str(willwere) + " 100 years old in the year " + str(ageToHundred + 2024) + ".")
