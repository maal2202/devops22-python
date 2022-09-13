# Lektion 6 - Övning 4
import random
import string
from operator import mul
from random import shuffle, choices, sample
from typing import Counter
from operator import itemgetter
from collections import deque

    # 1
names = ["adam", "bertil", "cesar", "david", "erik", "filip", "gustav", "helge", "ivar", "johan", "kalle", "ludvig"]
names50 = []
for i in range(50):
    names50.append(random.choice(names))

    # 2
queue = deque([], 10)

for i in range(10):
    queue.append(random.choice(names50))
print(queue)

    # 3
rand = random.randint(1, 10)
while rand > 0:
    queue.popleft()
    rand-=1
print(queue)

    # 4
refill = (10-len(queue))
finish = 40-refill
while refill > 0:
    queue.append(random.choice(names))
    refill-=1
print(queue)

    # 5
while finish > 10:
    queue.popleft()
    finish-=1
    queue.append(random.choice(names))
print(queue)
while finish > 0:
    queue.popleft()
    finish-=1
print(queue)