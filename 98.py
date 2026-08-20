# 98	Create a To-Do List application using Tkinter.
import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")

# Heading
heading = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 20, "bold")
)
heading.pack(pady=15)

# Entry box
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)


# Add task
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)


# Delete selected task
def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected)
    else:
        messagebox.showwarning("Warning", "Please select a task!")


# Clear all tasks
def clear_tasks():
    if task_list.size() > 0:
        task_list.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "The task list is already empty.")


# Task list
task_list = tk.Listbox(
    root,
    font=("Arial", 13),
    width=35,
    height=12
)
task_list.pack(pady=15)


# Buttons
add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task,
    width=15
)
add_button.pack(pady=5)

delete_button = tk.Button(
    root,
    text="Delete Task",
    command=delete_task,
    width=15
)
delete_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Clear All",
    command=clear_tasks,
    width=15
)
clear_button.pack(pady=5)


# Run application
root.mainloop()