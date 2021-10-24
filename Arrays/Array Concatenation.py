import array as arr

a = arr.array('i', [1,2,3,4,5,6,7,8,9,10]) #makes a array
b = arr.array('i', [11,12,13,14,15,16,17,18,19,20]) #makes a array
c = arr.array('i') #makes a array
d = arr.array('i') #makes a array
c = a + b #adds arrays to pre-existing array's
d = c + a #adds arrays to pre-existing array's

print('Array C =', c)
print('Array D =', d)
