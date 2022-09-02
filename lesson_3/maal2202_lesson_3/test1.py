X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
"Martin": "Sankt Eriksgatan 111",
"Bella": "Klockgatan 1",
"Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

print(f'X is of type {type(X)} and with a value of {X}')
print(f'Y is of type {type(Y)} and vwith a vlue of {Y}')

print(f'{addresses["Bella"]}')

addresses["Daniel"] = "Prinsgränd 2"

print(f'{addresses["Daniel"]}')

print(f'[2] dictionary {addresses}')

print(f'[3] list keys {list(addresses)}')

result_1 = len(addresses)
print(result_1)

print(f'Alphabetical {sorted(addresses)}')

antal = len(addresses)
print(f'Antal keys {antal}')


print(f'last value sorted (keys) {sorted(addresses)[-1]}')

last = sorted(addresses)[-1]
print(addresses[last])

addresses = {v: k for k, v in addresses.items()}
first = sorted(addresses)[0]
print(f'{addresses[first]}')

print(f'Cars is of type {type(cars)} and with a value of {cars}')

cars.append("Tesla")
cars.append("Audi")
print(f' cars {cars[Y]}')

cars.sort()
print(f'{cars[0]}')

cars_2 = cars
cars.append("Saab")

cars_3 = cars.copy()
print(cars_3)
cars.append("Ford")

print(f'cars: {cars}')
print(f'cars_2: {cars_2}')
print(f'cars_3: {cars_3}')

cars = cars*2

cars.sort()
cars.reverse()
print(cars)

unique_cars = cars
unique_cars = list(dict.fromkeys(unique_cars))
print(unique_cars)

print(f'numbers1 is of type {type(numbers1)} and with a value of {numbers1}')
print(f'numbers2 is of type {type(numbers2)} and with a value of {numbers2}')

print(numbers1)
print(numbers2)

#Set, dessa kan inte innehålla dubbletter (de tas bort)
print(f'Intersection of numbers1 and numbers2 {numbers1 & numbers2}')
print(f'Union of numbers1 and numbers2 {numbers1 | numbers2}')
print(f'Symmetriska differensen mellan numbers1 - numbers2 {numbers1 - numbers2}')
print(f'Synnetrusja differenseb mellan numbers2 - numbers1 {numbers2 - numbers1}')
print(f'Symmetriska differensen mellan numbers1 - numbers1 {numbers1 - numbers1}')