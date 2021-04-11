import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")
root.resizable(False,False)
root.title("Spin Box")

init_val = tk.StringVar(value=20)
spin_box = ttk.Spinbox(
    root,
    # values=(0,5,10,15,20,25,30),
    from_=0,
    to=30,
    textvariable=init_val,
    wrap= False
)
spin_box.pack()

print(spin_box.get())

root.mainloop()