import array as arr #impoty array

a = arr.array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
#make a Array (the first char is the type of the array) #i,s,f,d

print('Popping the number', a.pop()) #Will pop the last element in the array
print('Popping the number', a.pop(14)) #will pop the specific element(with the index code)
a.remove(14)#will remove the given number(without the index code and cannot be used with a print function)
print(a)
