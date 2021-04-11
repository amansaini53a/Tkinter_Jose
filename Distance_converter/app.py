import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
# root.geometry("400x400")
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

meter_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet Shown here: ")


def calculate_feet(*args):
    try:
        meters = float(meter_value.get())
        feet = meters * 3.28084
        feet_value.set(f"{feet: .3f}")
        # print(f"{meters} meters is equal to {feet: .3f} feet.")
    except ValueError:
        pass


root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

meter_label = ttk.Label(main, text="Meters: ")
meter_input = ttk.Entry(main, width=10, textvariable=meter_value, font=("Segoe UI",15))
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main, text="", textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

meter_label.grid(column=0, row=0, sticky="W")
meter_input.grid(column=1, row=0, sticky="EW")
meter_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

for child in main.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>")
root.mainloop()
