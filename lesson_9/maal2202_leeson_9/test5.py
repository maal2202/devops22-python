# Lektion 9 - Övning 5
from random import randint

class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

class Player(Person):
    def __init__(self, agi, spd, str):
        super().__init__(name, yob)
        self.agi = agi
        self.spd = spd
        self.str = str

    def __str__(self):
        return f"{self.name} - {self.yob} - {self.agi} {self.spd} {self.str}"

class Coach(Person):
    def __init__(self, voice):
        super().__init__(name, yob)
        self.voice = voice
    
    def __str__ (self):
        return f"{self.name} - {self.voice}"

class Team:
    def __init__(self, player, coach):
        self.player = player
        self.coach = coach

    def summarize(self):
        


def agility():
    return(randint(1, 10))

def speed():
    return(randint(1, 10))

def strenght():
    return(randint(1, 10))

def voice():
    return(randint(1, 10))
