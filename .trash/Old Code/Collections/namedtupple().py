from collections import namedtuple #imort named tupple from collections

_aa = namedtuple('UserCredidentials', 'Username, Password')
Username = _aa('Pranav', 'Asdfg')
print(Username)