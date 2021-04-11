import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness



set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

image = Image.open("aman_logo.png") #.resize((200,200))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo, padding=5, text="Hello", compound="right")
label.pack()
#############################################################################
# label = ttk.Label(root, text="Hello World", padding=20)
# label.config(font=("Segoe UI", 20))
# label.pack()
############################################################################
# greeting = tk.StringVar()
# label = ttk.Label(root, textvariable=greeting)
# label.pack()
# greeting.set("Hi")
############################################################################
root.mainloop()
