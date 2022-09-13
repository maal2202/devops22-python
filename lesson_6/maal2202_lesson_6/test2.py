# Lektion 6 - Övning 2
import random
import string
from operator import mul
from random import shuffle, choices, sample
from typing import Counter
from operator import itemgetter

    # 1
names = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"]
names_random = []
for i in range(100):
    names_random.append(random.choice(names))
print(names_random)

    # 2
c = Counter(names_random)
print(c)

    # 3
print(c.most_common(3))

    # 4
print(f'{c.most_common()[-1]}')

    # 5
names_unique = list(dict.fromkeys(names_random))

    # 5.1
alphabetical = sorted(names_unique)
print(alphabetical)

    # 5.2
random.shuffle(names_unique)
print(names_unique)

    # 5.3
alphabetical.reverse()
print(alphabetical)