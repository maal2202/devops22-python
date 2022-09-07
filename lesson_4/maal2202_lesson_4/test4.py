# Lektion 4 - Övning 4

start = int(input("Skriv siffran vi börjar med:\n"))
stop = int(input("Skriv siffran vi slutar med:\n"))

sum = 0
for x in range (start, stop):
    print(x)
    sum += x

print(sum)