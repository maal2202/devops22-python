# Lektion 8 - Övning 1

    # 1
def float_check(integer):
    try:
        integer / (integer-int(integer))
        print("It's a float")
    except ZeroDivisionError:
        print("It's an integer")
    return integer
float_check(5.1)