# Lektion 6 - Övning 7
from copy import copy, deepcopy

mylist = ["Adam", "Bertil", "Cesar", "David", "Erik"]
mycopy = copy(mylist)
mydeep = deepcopy(mylist)

mylist.pop()
mylist.append("Filip")

print(f'{mylist}\n{mycopy}\n{mydeep}')