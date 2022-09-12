# Lektion 6 - Övning 1

import random
import string
from operator import mul
from random import shuffle, choices, sample
from typing import Counter


# 1
list100 = []
for i in range(100):
    list100.append(i+1)
print(list100)

# 2
list60 = [x for x in list100[:60] if x % 2 == 0]
print(list60)

# 3
list77 = [x for x in list100[:77] if x % 2 != 0]
print(list77)

# 4
list300 = list(range(0,300))
    # 4.1
print(random.sample(range(0,300), 100))

    # 4.2
list300 = []
for i in range(100):
    n = random.randint(1,300)
    list300.append(n)
print(list300)

# 5
colors1 = ["green", "blue", "yellow", "pink", "purple"]

    # 5.1
colors2 = ["red"]
for i in range(2):
    colors2.append(random.choice(colors1))
print(colors2)

    # 5.2
colors3 = []
for i in range(50):
    colors3.append(random.choice(colors2))
print(colors3)

    # 5.3
colors1_unique = list(dict.fromkeys(colors1))
colors2_unique = list(dict.fromkeys(colors2))
colors3_unique = list(dict.fromkeys(colors3))
print(f'The lenght of list colors1 is {len(colors1)}, containing the colors {colors1_unique}')
print(f'The lenght of list colors2 is {len(colors2)}, containing the colors {colors2_unique}')
print(f'The lenght of list colors3 is {len(colors3)}, containing the colors {colors3_unique}')