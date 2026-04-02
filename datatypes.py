String = "spam", "Bob's", b"a\x01c", "sp\xc4m¹"
List = [1, [2, "three"], 4.5], list(range(10))
Tuple = (1, "spam", 4, "U"), tuple("spam"), "namedtup"
Dictionary = {"food": "spam", "taste": "yum"}, dict
hours = 10

print(String)
print(List)
print(Tuple)
print(Dictionary)
print(hours)
