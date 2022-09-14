# Lektion 7 - Övning 2
import string

    # 1
def ten(x=1, y=11):
    while x != y:
        print(x)
        x+=1
ten(10, 15)

    # 2
def string(word="A string", reverse=False):
    if reverse:
        word = word[::-1]
    print(word)
    # 4
string()
string(reverse=True)

# def string(reversed="reverse=False"):
#     string = "Hejhopp"
#     if reversed == "reverse=True":
#         print(f'{string[::-1]}, reverse=True')
#     else:
#         print(f'{string}, {reversed}')
# string("reverse=True")
# string()
# string("hejhoppppppp")

# def rev():
#     mystring = "Hejhopp"
#     print(f'{mystring[::-1]}')
#     print(f'{mystring}')
# rev()