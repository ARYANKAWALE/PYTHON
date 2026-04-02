a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Right Angled Triangle")
else:
    print("Not a Right Angled Triangle")