# Lektion 9 - Övning 3

class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return float(self.side * self.side)
    
    def circumference(self):
        return float(self.side * 4)
    
def main():

    square1 = Square(2)
    print(square1.area())
    print(square1.circumference())

    square2 = Square(3.5)
    print(square2.area())
    print(square2.circumference())

if __name__ == '__main__':
    main()