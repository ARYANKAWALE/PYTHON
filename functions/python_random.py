import random

print(random.randint(1, 10))
print(random.random())
print(random.choice(['A', 'B']))
items = [1, 2, 3]
random.shuffle(items)
print(items)