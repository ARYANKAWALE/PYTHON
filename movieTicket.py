age = int(input("Enter Your Age:"))
day = "Wednesday"
if age >= 18:
    price = 12
else:
    price = 8
if day == "Wednesday":
    price =  price - 2
    print("Discoint Applied: -2$ for Wednnesday")
print(f"Your final ticket price is: ${price}")