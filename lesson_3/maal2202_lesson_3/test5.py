# Övning5 - Sorting

cars = []
cars.extend(["volvo", "saab", "audi", "bmw", "porche", "ferrari", "lotus", "ford", "tesla", "nio"])

print(f'ordinarie inmatning {cars}')

# Koden för sorted() och reversed() genererar endast sortering sagd kod
print(f'sorted {sorted(cars)}')
print(f'reversed {list(reversed(cars))}')

print(f'ordinarie inmatning {cars}')

# Sorteringen ifrån .sort och .reverse behålls fortsatt nedåt i koden
cars.sort()
print(f'efter cars.sort() {cars}')

cars.reverse()
print(f'efter cars.reverse() {cars}')

print(f'Sorteringen är fortsatt baklänges {cars}')