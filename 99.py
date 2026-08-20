# 99	Create a Number Guessing Game with GUI.
import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0


# Check the guess
def check_guess():
    global attempts

    try:
        guess = int(entry.get())
        attempts += 1

        if guess < 1 or guess > 100:
            messagebox.showwarning(
                "Invalid Input",
                "Enter a number between 1 and 100."
            )
            return

        if guess < secret_number:
            result_label.config(text="Too Low! Try again.")

        elif guess > secret_number:
            result_label.config(text="Too High! Try again.")

        else:
            messagebox.showinfo(
                "Congratulations!",
                f"You guessed it!\n"
                f"The number was {secret_number}.\n"
                f"Attempts: {attempts}"
            )
            result_label.config(text="You Won! 🎉")
            guess_button.config(state="disabled")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )


# Start a new game
def new_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    entry.delete(0, tk.END)
    result_label.config(text="Guess a number between 1 and 100")
    guess_button.config(state="normal")


# Create window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x350")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="Number Guessing Game",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

# Instructions
instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 12)
)
instruction_label.pack(pady=10)

# Entry
entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    width=15
)
entry.pack(pady=10)

# Guess button
guess_button = tk.Button(
    root,
    text="Guess",
    font=("Arial", 12, "bold"),
    width=15,
    command=check_guess
)
guess_button.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="Make your first guess!",
    font=("Arial", 12)
)
result_label.pack(pady=10)

# New game button
new_game_button = tk.Button(
    root,
    text="New Game",
    font=("Arial", 11),
    width=15,
    command=new_game
)
new_game_button.pack(pady=15)

# Run application
root.mainloop()