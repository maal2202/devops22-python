# Lektion 6 - Övning 5
from math import sqrt
from collections import namedtuple
from re import X

mytuple = namedtuple('Coordinates', ['x', 'y'])

dot1 = mytuple(x=4, y=6)
dot2 = mytuple(x=1, y=2)

board = [["-"]*10 for i in range(10)]

board[dot1.x][dot1.y] = 'X'
board[dot2.x][dot2.y] = 'O'

for row in board:
    print(row)

print(dot1.x-dot2.x)
print(dot1.y-dot2.y)

a = (dot1.x-dot2.x)
b = (dot1.y-dot2.y)
c = (a*a)+(b*b)
print(sqrt(c))