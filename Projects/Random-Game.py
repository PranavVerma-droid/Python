import random
guess = 0
print('Welcome to my guessing game. My name is Jiksaw.')
print('You have to guess the correct number and enter it in the terminal.')
print('The Max number for Guessing will be what you select as the number''( That means the number will not go above what you specify)')
print('if you want to quit at any time, pls type the number 0')
print('Go ahead and type the Number Bellow. viel Glück!!')


max = int(input('Pls Specify the Max number to Start: '))
what_to_guess = int(max * random.random()) + 1
while guess != what_to_guess:
    guess = int(input('New Number: '))
    if guess > 0:
        if guess > what_to_guess:
            print('Number is too large!')
        elif guess < what_to_guess:
            print('Number is too small!')
    else:
        print('Sorry that you are giving up!! The Number was',what_to_guess)
        break

else:
    print('Congrats you found the number!!! It was in fact the number',what_to_guess,'!!')