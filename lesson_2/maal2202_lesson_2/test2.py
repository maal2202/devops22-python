# Test 2 inputs

# Variabler
from tkinter import N


name = input("What is your name?\n")
print(f'Hello {name}, good morning')

# Skriver ut vilken typ variabeln är, i detta fall string (class 'str')
print(f'Name is of type {type(name)}')

# Variabel för ålder, med input
age = input(f'How old are you {name}?\n')
print(f'Name is of type {type(age)}')
print(f'Times two that is {int(age)*int(2)}')

# Print a string times two
greet = input(f'How do you greet people? {name}?\n')
print(f'Oh! {greet * 2}')

# Print a float input and divid it by 3.5
zip = input(f'What is your zipcode {name}?\n')
print(f'that divided by 3.5 is {float(zip)/3.5}')
