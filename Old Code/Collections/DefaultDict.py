from collections import defaultdict #imports Defaultdict from collections

a = defaultdict(int) #make a defaultdict
a[1] = 'python' #set some variables
a[2] = 'Pranav' #set some variables

print(a[3])
# in a defaultdict, it will ignore the errors when a key is not present in a dictonary.
#The output will be one (if data is not present)
