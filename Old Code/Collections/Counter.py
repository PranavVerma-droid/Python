from collections import Counter #imports Counter from collections

_a0 = [1,2,3,1,2,2,3,1,1,1,1,2,2,3,3,3,4,4,4,5] #make a list/tupple
_a00 = Counter(_a0) #make a counter
sub = {1:2 , 2:1}
print(_a00) #print the counter
print(list(_a00.elements())) #gives us all the individual elements in the list/tupple
print(_a00.most_common()) #gives us the number of elements in the list in decending order
print(_a00.subtract(sub))#Substracts the given numbers from the list
print(_a00.most_common()) #gives us the number of elements in the list in decending order
