password = "a@342"

if len(password) < 6:
    Strength = "Weak"
elif len(password) < 10:
    Strength = "Medium"
else:
    Strength = "Strong"

print("Print strength is:", Strength)