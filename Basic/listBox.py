import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")
root.title("List Box")
root.resizable(False,False)

p_lang = ("C", "C++", "Python", "Java", "Go")

lang = tk.StringVar(value=p_lang)

lang_select = tk.Listbox(root, listvariable=lang, height=len(p_lang))
lang_select["selectmode"] = "extended"
lang_select.pack()


def handle(event):
    selected_indices = lang_select.curselection()
    for i in selected_indices:
        print(lang_select.get(i))


lang_select.bind("<<ListboxSelect>>", handle)

root.mainloop()