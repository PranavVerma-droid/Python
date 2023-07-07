My_Dict = {'Pranav':'001','Ananiya':'002','Student3':'003','Student4':'004'}

print(My_Dict['Pranav']) #Gets the value to the specific keys given in the Dict
My_Dict.keys()#use with a print command to see all the keys in a dict
My_Dict.values()#use with a print command to see all the value's in a dict

for x,y in My_Dict.items():
    print(x,y)
for z in My_Dict:
    print(z)

My_Dict['Pranav'] = '005' #change specific files in a dict
My_Dict['Pranav'] = '001' #change specific files in a dict
My_Dict['Student5'] = '006' #if key is present it will change value in the key or if not present it will add to the dict
My_Dict.pop('Student5') #will pop the specific key and its value from the Dict
My_Dict['Student5'] = '006' #if key is present it will change value in the key or if not present it will add to the dict
My_Dict.popitem()#WIll pop the last item in the Dict(Being 'Student5')
My_Dict['Student5'] = '006' #if key is present it will change value in the key or if not present it will add to the dict
del My_Dict['Student5'] #will remove the specified item ket and its value
print(My_Dict)






