# 97	Create a GUI calculator using Tkinter.
import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")


# Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10
)
display.pack(fill="both", padx=10, pady=10, ipady=10)


# Functions
def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2)
]

frame = tk.Frame(root)
frame.pack()

for text, row, column in buttons:
    button = tk.Button(
        frame,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=lambda value=text: click(value)
    )
    button.grid(row=row, column=column, padx=2, pady=2)

# Clear button
tk.Button(
    frame,
    text="C",
    font=("Arial", 18),
    width=5,
    height=2,
    command=clear
).grid(row=4, column=3, padx=2, pady=2)

# Equals button
tk.Button(
    frame,
    text="=",
    font=("Arial", 18),
    width=22,
    height=2,
    command=calculate
).grid(row=5, column=0, columnspan=4, padx=2, pady=5)

root.mainloop()