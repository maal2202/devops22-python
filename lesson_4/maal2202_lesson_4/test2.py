# Lektion 4 - Övning 2

vip = ("Adam", "Bertil", "Ceasar", "David", "Erik")

name = input("Skriv ett namn: ").title()

if name in vip:
    print(f"Welcome {name} You are on the list")
else:
    print(f"{name} you are not on the list")