from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
def show():
    print(e.get())

Button(root,text="show", command=show).pack()
root.mainloop()