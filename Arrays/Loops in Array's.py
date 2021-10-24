import array as arr

temp = 0
tem = 0
a = arr.array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) #make a array

for y in a:
    print(y)
for x in a[0:5]:
    print(x)

while temp<a[2]:    #While 0(CALLED TEMP HERE) is smaller then 2 in the array, its gonna keep adding to 0 until it is
    print(a[temp])  #Equal to 0
    temp = temp + 1
while tem<len(a):
    print(a[tem])
    tem+=1


