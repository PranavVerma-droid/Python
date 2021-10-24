x = 19
y = 20
list = [19,29,30,220]

if x == y:
    print('equal') #if x is equal to y then it will execute this list and leave the others or move on
elif x > y:
    print('greater') #if x is greater than y and it will execute this list and leave the others or move on
else:
    print('smaller') #if x is smaller than y this will execute and continue with the script

x > 5 and x > 20
#And operator is used when both the statements will have to be true then the output will be true or false

x > 5 or x > 20
#Or operator is used when only one of the statements are true then output will be true or false

not(x > 5 and x > 20)
#Not operator negates the output (basically reverses the output)

x is y #If x is equal to y then true else false
x is not y #if x is not equal to y then true else false

x in list #will be true if variable 'x' is present in list
x not in list #will be true if variable 'x' is NOT present in list