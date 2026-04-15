import tkinter as tk

app = tk.Tk()
app.title("Image Window")
img = tk.PhotoImage(file="my_image.png")
image_label = tk.Label(app, image=img)
image_label.pack()

app.mainloop()