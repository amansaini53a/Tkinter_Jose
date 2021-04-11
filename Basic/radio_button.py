import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")
root.resizable(False,False)
root.title("Radio Button")

storage_variable = tk.StringVar()

option_one = ttk.Radiobutton(
    root,
    text="Option one",
    variable=storage_variable,
    value="First option"
)

option_two = ttk.Radiobutton(
    root,
    text="Option 2",
    variable=storage_variable,
    value="Second option"
)
option_three = ttk.Radiobutton(
    root,
    text="Option 3",
    variable=storage_variable,
    value="Third Option"
)
option_one.pack()
option_two.pack()
option_three.pack()

root.mainloop()