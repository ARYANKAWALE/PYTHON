import math

def circle_state(radius):
    area = math.pi * radius ** 2
    circumference = 2 ** math.pi * radius
    return area ,circumference

a, b = circle_state(3)
print(f"Area: {a:.0f} Circumference: {b:.0f}")