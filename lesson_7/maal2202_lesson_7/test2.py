# Lektion 7 - Övning 2
import string

    # 1
def ten(x=1, y=11):
    while x != y:
        print(x)
        x+=1
ten(20, 25)

    # 2
def string(reversed="reverse=False"):
    string = "Hejhopp"
    if reversed == "reverse=True":
        print(f'{string[::-1]}, reverse=True')
    else:
        print(f'{string}, {reversed}')
string("reverse=True")
string()
string("hejhoppppppp")
# Oklart om ovan är korrekt, räknas detta som "used as an argument, då reverse=True måste skrivas som en string i funktionen"

# def rev():
#     mystring = "Hejhopp"
#     print(f'{mystring[::-1]}')
#     print(f'{mystring}')
# rev()