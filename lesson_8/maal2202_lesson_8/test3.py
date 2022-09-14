# Lektion 7 - Övning 3

def div(x, y):
    try:
        result = x / y
    except TypeError:
        print('String is not allowed')
    except ZeroDivisionError:
        print(f'Division by 0 is not allowed')
    else:
        return result

print(div(10, "0"))