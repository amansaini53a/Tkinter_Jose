import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("400x400")
root.resizable(False, False)
root.title("Check Box")

# check_button = ttk.Checkbutton(root, text="Check Button 1")
# check_button.pack()
# check_button["state"] = "disabled"

selected_option = tk.StringVar()


def print_current_option():
    print(selected_option.get())


check = tk.Checkbutton(
    root,
    text="Check me",
    variable=selected_option,
    command=print_current_option,
    onvalue="On",
    offvalue="Off"
)
check.pack()

root.mainloop()
