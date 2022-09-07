# Lektion 4 - Övning 5

stop = str(input('Skriv ett ord (för att sluta, skriv "stop")\n'))

while stop != str("stop"):
    print(f'{stop} innehåller {len(stop)} karaktärer. \n')
    stop = str(input('Skriv ett ord (för att sluta, skriv "stop")\n'))

while True:
    if(stop == str("stop")):
        break
    print(stop)