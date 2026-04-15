try:
    f = open("file.txt","r")
    print(f.read())
except:
    print("File not available")
else:
    f.close()
    print("File closed..!")