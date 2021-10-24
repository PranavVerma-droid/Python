import pandas as panda

Nest_Dict = {'Emploee':{'Dave':{'ID':'0023','Salary':'23000'},'Ava':{'ID':'0024','Salary':'23000'},
            'Pranav':{'ID':'0025','Salary':'1000000'}}}

a = panda.DataFrame(Nest_Dict['Emploee'])
print(a)

