from tkinter import *
root = Tk()
def submit():
    print("Submitted")

b = Button(root,text="Submit", command=submit)
b.pack()
root.mainloop()