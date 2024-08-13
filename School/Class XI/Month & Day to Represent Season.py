winter = ["October", "November", "December", "January", "February"]
spring = ["March", "April"]
summer = ["May", "June", "July"]
autumn = ["August", "September"]

monthInput = str(input("Please Enter Month Name: "))
dayInput = int(input("Please Enter Day: "))

if (dayInput > 0) and (dayInput <= 31):
    if monthInput in winter:
        print("Winter.")
    elif monthInput in spring:
        print("Spring.")
    elif monthInput in summer:
        print("Summer.")
    elif monthInput in autumn:
        print("Autumn.")
    else:
        print("Please Enter a Vaild Month Name.")
else:
    print("Please Enter a Vaild Day in the Month.")
