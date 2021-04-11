import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass



def greet():
    print(f"Hello {user_name.get() or 'World'} ")


root = tk.Tk()
user_name = tk.StringVar()

imput_frame = ttk.Frame(root, padding= (20,10,20,0))
imput_frame.pack(fill= 'both')
name_label = ttk.Label(imput_frame, text='Name: ').pack(side='left', padx=(0, 10))
name_entry = ttk.Entry(imput_frame, width=15, textvariable=user_name).pack(side='left')

buttons = ttk.Frame(root, padding= (20,10)).pack(fill= 'both')
ttk.Button(buttons, text='Greet', command=greet).pack(side='left', fill='both', expand=True)
ttk.Button(buttons, text="Quit", command=root.destroy).pack(side='right')

root.mainloop()
