from tkinter import *

root = Tk()

img = PhotoImage(file="image.png")
Label(root, image=img).pack()

root.mainloop()
