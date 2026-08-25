# Generate a random number between 1 and 100. Allow limited attempts and provide hints like "Too High" or "Too Low."
import random

def play_number_guessing_game():
    target_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        if guess < 1 or guess > 100:
            print("Please pick a number between 1 and 100.")
            continue

        attempts += 1

        if guess == target_number:
            print(f"🎉 Congratulations! You guessed the correct number ({target_number}) in {attempts} attempts!")
            return
        elif guess < target_number:
            print("📉 Too Low!")
        else:
            print("📈 Too High!")

    print(f"\n❌ Game Over! You've used all {max_attempts} attempts. The number was {target_number}.")

# Start the game
play_number_guessing_game()