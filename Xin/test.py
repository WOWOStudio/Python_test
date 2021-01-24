import random

count = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

for i in range(1000):
    choice = random.choice(list(count.keys()))
    count[choice] += 1
print(count)
