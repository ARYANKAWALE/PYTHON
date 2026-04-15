import tkinter as tk

app = tk.Tk()
tk.Label(app, text="Username:").pack()
u = tk.Entry(app)
u.pack()
tk.Label(app, text="Password:").pack()
p = tk.Entry(app, show="*")
p.pack()

tk.Button(app, text="Login").pack()

app.mainloop()
