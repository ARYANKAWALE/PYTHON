a = int(input("Enter a:"))
b = int(input("Enter b:"))
try:
    c = a/b
    print("a/b = %d" %c)
except ZeroDivisionError:
    print("Division by zero is not allowed")

#other code:
print("Hi I am other part of the program")