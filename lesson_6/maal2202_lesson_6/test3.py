# Lektion 6 - Övning 3
import string
from operator import mul
from random import shuffle, choices, sample
from typing import Counter

    # 1
the_list = list(string.ascii_lowercase)
print(the_list)

    # 2
the_stack = []
n=0
for item in the_list:
    the_stack.append(the_list[n])
    n+=1
print(the_stack)

    # 3
# for item in the_list:
#     the_stack.pop()
# print(the_stack)

# lengt = len(the_stack)+1
# while lengt > 0:
#     print(the_stack)
#     the_stack.pop()
#     lengt-=1

while len(the_stack) > 0:
    print(the_stack)
    the_stack.pop()
print(the_stack)