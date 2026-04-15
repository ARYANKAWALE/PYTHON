import tkinter as tk

def solve():
    try:
        result_label.config(text = "Answer: " + str(eval(box.get())))
    except:
        result_label.config(text = "Error! Invalid math.")
app = tk.Tk()
box = tk.Entry(app, font=("Arial", 16))
box.pack(pady=10)
tk.Button(app, text="Calculate", command=solve).pack()
result_label = tk.Label(app, text="Answer will appear here", font=("Arial", 14))
result_label.pack(pady=10)

app.mainloop()