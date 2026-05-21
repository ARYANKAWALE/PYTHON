from tkinter import *
def hello():
    print("Button clicked")

root = Tk()
b = Button(root, text="Click", command=hello)
b.pack()
root.mainloop()
