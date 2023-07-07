"""Arguments In Python"""

def greet(name):
    print('Hello', name)
    print('How do u do?')

greet("Pranav")
#here is a little tutorial for functions in python: 
#https://www.youtube.com/watch?list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn&v=-Bkupx9gX0o&ab_channel=Programiz


"""Adding Numbers Using Functions"""

def add_numbers(n1, n2):
    result = n1 + n2
    return result

result = add_numbers(15, 16)
print(result)