import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("400x400")
root.resizable(False,False)
root.title("Separators")

ttk.Label(root, text="Hello World", padding=20).pack()

ttk.Separator(root, orient= "horizontal").pack(fill="x")

ttk.Label(root, text="Aman Saini", padding=20).pack()
root.mainloop()