import array as arr #impoty array

a = arr.array('i', [1,2,3,4,5,6,7,8,9,10,10]) #make a Array (the first char is the type of the array) #i,s,f,d

a.append(12) #adds the value to the end of the array
a.insert(12,13) #adds the value to a specific point in the array
a.extend([14, 15, 16]) #extends the append using the given value's at the end(Use with square brackets)
print(a)

