import random

print(random.randint(1, 10))        # Random integer (1-10)
print(random.random())              # Random float (0.0-1.0)
print(random.choice(['A', 'B']))    # Pick random item
items = [1, 2, 3]
random.shuffle(items)               # Shuffle list in-place
print(items)