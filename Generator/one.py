def numbers():
    yield 1
    yield 2
    yield 3
g = numbers()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
