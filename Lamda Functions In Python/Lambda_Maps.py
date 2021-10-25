#map(func, iterables)
mylist = [1,2,3,4,5,6]
p = list(map(lambda a:(a/3 != 2), mylist)) 
"""Map will specify the expression with mylist with the boolean values"""
print(p)