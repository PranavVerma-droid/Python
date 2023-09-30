mylist = [1,2,3,4,5,6] #make a list
newlist = list(filter(lambda a:(a/3 == 2), mylist)) #SYNTAX: filter(function, iterables)
newlist2 = list(filter(lambda b:(b/3 == 1), mylist)) #SYNTAX: filter(function, iterables)
print(newlist) #prints the list
print(newlist2) #prints the list
"""This Code will check for any iterables in mylist for anything that can divide with a to give a output of 2"""
