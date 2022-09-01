# Test 2 inputs

# Variabler
name = input("What is your name?\n")
print(f'Hello {name}, good morning')

# Skriver ut vilken typ variabeln är, i detta fall string (class 'str')
print(f'Name is of type {type(name)}')

# Variabel för ålder, med input
age = input(f'How old are you {name}?\n')
print(f'Age is of type {type(age)}')
if age.isdigit():
    print (f'Oh so young, I am double your age, {int(age)*2}')
else:
    print (f'{name} you are so dumb!')

# Print a string times two
greet = input(f'How do you greet people? {name}?\n')
print(f'Oh! {greet * 2}')

# Print a float input and divid it by 3.5
zip = input(f'What is your zipcode {name}?\n')
if zip.isdigit():
    print(f'that divided by 3.5 is {float(zip)/3.5}')
else:
    print(f'Syntax error, do not compute! Good bye {name}!')