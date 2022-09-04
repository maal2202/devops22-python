# Uppgift B, lektion 3

# Person_1
name1 = input("Name of person 1:\n>")
age1 = input("How old is person 1:\n>")
shoe1 = input("Shoe size of person 1:\n>")

# Person_2
name2 = input("Name of person 2:\n>")
age2 = input("How old is person 2:\n>")
shoe2 = input("Shoe size of person 2:\n>")

# Person_3
name3 = input("Name of person 3:\n>")
age3 = input("How old is person 3:\n>")
shoe3 = input("Shoe size of person 3:\n>")

#Tuple av de tre personerna
tup = [(name1, age1, shoe1), (name2, age2, shoe2), (name3, age3, shoe3)]
print(tup)

tup.sort(key=lambda y: y[1])
tup.reverse()
print(f'The oldet person is {max(tup[0])} with a shoe size of {max(tup[0])}')

#for item in tup:
#print(f' The oldest person is {max(tup[0])}')

# print ("Max value element : ", max(tup))

#name = input("What is your name?\n")
#print(f'Hello {name}, good morning')

# Skriver ut vilken typ variabeln är, i detta fall string (class 'str')
#print(f'Name is of type {type(name)}')

# Variabel för ålder, med input
#age = input(f'How old are you {name}?\n')
#print(f'Age is of type {type(age)}')
#if age.isdigit():
#    print (f'Oh so young, I am double your age, {int(age)*2}')
#else:
#    print (f'{name} you are so dumb!')

# Print a string times two
#greet = input(f'How do you greet people? {name}?\n')
#print(f'Oh! {greet * 2}')

# Print a float input and divid it by 3.5
#zip = input(f'What is your zipcode {name}?\n')
#if zip.isdigit():
#    print(f'that divided by 3.5 is {float(zip)/3.5}')
#else:
#    print(f'Syntax error, do not compute! Good bye {name}!')