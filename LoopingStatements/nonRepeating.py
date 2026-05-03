input_string = "aryan"
for char in input_string:
    print(char)
    if input_string.count(char) == 1:
        print("Non repeating string is:",char)
        break