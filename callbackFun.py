def square(x):
    return x * x

def number(num, callback):
    return callback(num)

result = number(5, square)
print(result)