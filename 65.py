# Create a menu-driven dictionary application.
def display_menu():
    print("\n" + "=" * 30)
    print("      DICTIONARY APPLICATION")
    print("=" * 30)
    print("1. Search for a Word")
    print("2. Add a New Word")
    print("3. Update an Existing Definition")
    print("4. Delete a Word")
    print("5. Display All Words")
    print("6. Exit")
    print("=" * 30)

def main():
    # Initial dictionary dataset
    dictionary = {
        "python": "A high-level, interpreted programming language.",
        "algorithm": "A step-by-step procedure for solving a problem.",
        "variable": "A reserved memory location to store values.",
        "function": "A block of organized, reusable code used to perform a single action."
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            # Search for a word
            word = input("Enter word to search: ").strip().lower()
            if word in dictionary:
                print(f"\n📖 **{word.capitalize()}**: {dictionary[word]}")
            else:
                print(f"\n❌ '{word}' was not found in the dictionary.")

        elif choice == '2':
            # Add a new word
            word = input("Enter new word: ").strip().lower()
            if word in dictionary:
                print(f"\n⚠️ '{word}' already exists. Use Option 3 to update it.")
            else:
                definition = input("Enter definition: ").strip()
                dictionary[word] = definition
                print(f"\n✅ '{word.capitalize()}' added successfully!")

        elif choice == '3':
            # Update a definition
            word = input("Enter word to update: ").strip().lower()
            if word in dictionary:
                print(f"Current definition: {dictionary[word]}")
                new_def = input("Enter new definition: ").strip()
                dictionary[word] = new_def
                print(f"\n✅ Definition for '{word.capitalize()}' updated successfully!")
            else:
                print(f"\n❌ '{word}' was not found.")

        elif choice == '4':
            # Delete a word
            word = input("Enter word to delete: ").strip().lower()
            if word in dictionary:
                del dictionary[word]
                print(f"\n🗑️ '{word.capitalize()}' deleted successfully!")
            else:
                print(f"\n❌ '{word}' was not found.")

        elif choice == '5':
            # Display all words
            if not dictionary:
                print("\n📭 The dictionary is currently empty.")
            else:
                print("\n--- ALL DICTIONARY ENTRIES ---")
                for word, definition in sorted(dictionary.items()):
                    print(f"• **{word.capitalize()}**: {definition}")

        elif choice == '6':
            # Exit
            print("\nGoodbye! 👋")
            break

        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()