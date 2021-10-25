#reduce(function,sequence)
from functools import reduce #Also you can use import functools or from functools import *
X = reduce(lambda a, b: a + b, [23,56,43,98,1]) #will add all of these digits recursively (One-By-One)
print(X)