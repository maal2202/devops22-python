# Lektion 7 - Övning 2

def check_even(num):
    if (num % 2) == 0:
        raise Exception("Even numbers not allowed")

def ask_number(number):
    ask = None
    while True:
        try:
            ask = int(input(number))
            check_even(ask)
            break
        except ValueError:
            print("Sorry, not an int")
        except Exception:
            print("Even numbers not allowed")
    return ask

user_number = ask_number("Chose your number: ")
print(user_number)