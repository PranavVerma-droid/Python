from collections import deque #imort deque tupple from collections

a = ['P', 'r', 'a', 'n', 'a', 'v']
d = deque(a) #forms a deque

d.append('Learns Python') #adds to the right of the list
d.appendleft('Learns Python') #adds to the left of the list
print(d)
d.pop() #removes a value from the right of the list
d.popleft() #removes a value from the right of the list
print(d)