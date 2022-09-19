# Lektion 9 - Övning 2

class Animal:
    def __init__(self, family):
        self.family = family

class Dog(Animal):
    def __init__(self, breed, sex):
        self.breed = breed
        self.sex = sex

class Supermarket:
    def __init__(self, location, open, close):
        self.location = location
        self.open = open
        self.close = close

class Coop:
    def __init__(self, location, open, close, type):
        self.location = location
        self.open = open
        self.close = close
        self.type = type