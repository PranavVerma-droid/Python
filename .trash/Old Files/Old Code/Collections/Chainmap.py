from collections import ChainMap #imports Chainmap from collections

a = {1: '3' , 2: '4'}#Chainmap helps us to sort out dictonaries, lists and tupples
b = {3: '1' , 4: '2'}#Chainmap helps us to sort out dictonaries, lists and tupples
c = ['Apple', 'banana']#Chainmap helps us to sort out dictonaries, lists and tupples
e = (1,2,3,4,5,6)#Chainmap helps us to sort out dictonaries, lists and tupples

_a = ChainMap(a,b,c,e) #make a chainmap
print(_a) #print a chainmap