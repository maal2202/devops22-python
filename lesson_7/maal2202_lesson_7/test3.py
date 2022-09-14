# Lektion 7 - Övning 3

    # 1
def addition(x, y):
    return (x+y)
print(addition(10, 5))

    # 2
def mytuple(x, y):
    return x, y
print(mytuple(10,5))

    # 3
def boolean(x, y):
    return x > y
print(boolean(2, 4))
# eller
def bool():
    return False

    # 4
def float():
    return 1.5
print(float())

    # 5
def fullname(first, last):
    return first.title(), last.title()
print(f'{fullname("MARTIN", "ALFREDSon")}')

    # 6
def rect(x, y):
    return x*y
print(rect(10,5))

    # 7
def summa(total):
    return sum(total)
print(summa((100, 300, 200)))

    # 8
def repeat(word, repeat):
    for r in range(repeat):
        print(word)
repeat("Hej", 5)