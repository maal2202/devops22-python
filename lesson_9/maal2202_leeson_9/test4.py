# Lektion 9 - Övning 4
from cgitb import grey
from math import pi

class Circle:

    def __init__(self, diagonal):
        self.diagonal = diagonal
        self.color = "grey"
        self.area = self.calcarea()
        self.circumference = self.calccircumference()

    def calcarea(self):
        return (pi*(self.diagonal/2))**2

    def calccircumference(self):
        return self.diagonal*pi
    
    def changecolor(self, color):
        self.color = color

def main():

    circle1 = Circle(5)
    print(circle1.area)
    print(circle1.circumference)
    print(circle1.color)
    circle1.changecolor("green")
    print(circle1.color)

if __name__ == '__main__':
    main()