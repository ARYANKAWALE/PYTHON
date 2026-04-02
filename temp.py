print("Temperature Converter")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = input("Enter your choice (1/2): ")
if choice == '1':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * (5/9)
    print(f"{f} F is {c:.2f} C")
elif choice == '2':
    c = float(input("Enter temperature in Celsius: "))
    f = (c * (9/5)) + 32
    print(f"{c} C is {f:.2f} F")
else:
    print("Invalid choice. Please enter 1 or 2.")