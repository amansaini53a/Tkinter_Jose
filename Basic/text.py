import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("Widgets Example")

text = tk.Text(root, height=8)
text.pack()
# 1 is line number,  0 is the character number.Means 1st line 1 char.
text.insert("1.0", "Please enter a comment...")
# Make the above line fixed
text["state"] = "disabled"  # "normal"

text_content = text.get("1.0", "end")  # start pos and end pos
print(text_content)
root.mainloop()
