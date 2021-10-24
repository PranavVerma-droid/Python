#Dictonary's can contain strings, integers and even floats.
Dictonary = {'Username': 'Pranav234',
             'Password': 'AQWASWEDRF'}

print(Dictonary)
print(Dictonary['Username'])#can be used to print specific place of the list from index number xD
print(Dictonary['Password'])#can be used to print specific place of the list from index number xD
print(Dictonary.get('Username'))#can be used to print specific place of the list from index number xD

#say if i needed to change the pass??
Dictonary['Password'] = 'AFGHJKLOIU'
print(Dictonary['Password'])

#say if i needed to add another account???
Dictonary['Username2'] = 'Pranav235'
Dictonary['Password2'] = 'ASDASDASDASDASD'
print(Dictonary)
