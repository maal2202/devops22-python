# Lektion 7 - Övning 1
from audioop import reverse
import string
    # 1
def do_nothing():
    pass
do_nothing()
    # 2.1
def hello_world():
    print("Hello World")
hello_world()
    # 2.2
def result():
    print(1==1.0)
result()
    # 2.3
def abc():
    abc = list(string.ascii_lowercase)
    abc.sort(reverse=True)
    print(abc)
abc()
    # 3.1
def greet(name):
    print(f'Hello {name}')
greet("Pelle")
    # 3.2
def yell(word):
    print(word.upper())
yell("hej")
    # 3.4
def numbers(stop):
    print(list(range(1, stop)))
# Tidigare lösning, svar given i solutions använd ovan
# def numbers(stop):
#     start = 1
#     while stop != start:
#         print(start)
#         start += 1
numbers(7)