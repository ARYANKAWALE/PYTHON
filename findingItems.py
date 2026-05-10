items = ["laptop", "mouse", "keyboard", "monitor"]

for item in items:
    if item == "keyboard":
        print("Found the keyboard!")
        break # No need to keep looking
    print(f"Checking {item}...")