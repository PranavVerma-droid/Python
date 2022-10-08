#Lists are like Dictonary's but thet cannot define themselves, can contain strings, tupples, floats, and integers

List = ['Pranav', 20, 30, 40, 30, (20, 30, 30)] #a list is written like this
print(List)


List.insert(3, 'MyString') #Insert adds to a specific location to the list
List.append('Append Addes to the LAST of the list') #.append adds to the last of the list (always)
print(List)

List.reverse() #Reverse's the list
print(List[2]) #can be used to print specific place of the list from index number xD

a = [1,2,3]
b = {1: 'Key',
     2: 'Pass'}
c = [a,b]


print(c)#you can use a list with other data types like dict's and lists.

#also, index's  are used in lists, tupples and dictonary's. they start with a 0 and go till the end of the string