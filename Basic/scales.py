import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scales")
root.geometry("400x400")
root.resizable(False, False)


def handle(event):
    print(scale.get())


current_value = tk.DoubleVar()

scale = ttk.Scale(
                  root,
                  orient="horizontal",
                  from_=0,
                  to=10,
                  command=handle,
                  variable=current_value
                )

scale.pack(fill="x")
#scale["state"] = "disabled" #normal


root.mainloop()
