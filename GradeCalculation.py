score = int(input("Enter Your Score:"))

if score > 100:
    print("Please verify your score")
    exit()

if score >= 90:
    print("A Grade")
elif(score >= 80):
    print("B Grade")
elif(score >= 70):
    print("C Grade")
elif(score >= 60):
    print("D Grade")
else:
    print("F Grade")