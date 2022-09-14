# Lektion 7 - Övning 3

# def check_string(num):
#     if type(num) == str:
#         raise Exception("String is not allowed")

def div(x, y):
    try:
        result = x / y
        return result
    except TypeError:
        print(f'TypeError, string is not allowed')
    except ZeroDivisionError:
        print(f'Division by 0 is not allowed')
    
    # if type(y) == str:
    #     raise TypeError("String is not allowed)")
    # except TypeError:
    #     print("String is not allowed")

print(div(10, 0))