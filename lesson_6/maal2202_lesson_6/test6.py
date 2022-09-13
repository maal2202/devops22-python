# Lektion 6 - Övning 6
from copy import copy

mystring = "My String"

mystring2 = mystring

mystring3 = copy(mystring)

mystring2 = "New String"

print(f'{mystring, mystring2, mystring3}')