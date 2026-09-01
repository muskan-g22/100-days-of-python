
# Perform various string operations using a menu:

# Reverse
# Capitalize
# Title Case
# Replace
# Count occurrences
# Remove spaces

def reverse_string(s: str) -> str:
    return s[::-1]

def capitalize_string(s: str) -> str:
    return s.capitalize()

def title_case_string(s: str) -> str:
    return s.title()

def replace_in_string(s: str, old: str, new: str) -> str:
    return s.replace(old, new)

def count_occurrences(s: str, sub: str) -> int:
    return s.count(sub)

def remove_spaces(s: str) -> str:
    return s.replace(" ", "")

def main():
    text = input("Enter a string: ")

    while True:
        print("\nChoose an operation:")
        print("1. Reverse")
        print("2. Capitalize")
        print("3. Title Case")
        print("4. Replace")
        print("5. Count occurrences")
        print("6. Remove spaces")
        print("7. Change input string")
        print("8. Exit")

        choice = input("Enter choice (1–8): ").strip()

        if choice == "1":
            print("Reversed:", reverse_string(text))
        elif choice == "2":
            print("Capitalized:", capitalize_string(text))
        elif choice == "3":
            print("Title Case:", title_case_string(text))
        elif choice == "4":
            old = input("Substring to replace: ")
            new = input("Replacement substring: ")
            print("Result:", replace_in_string(text, old, new))
        elif choice == "5":
            sub = input("Substring to count: ")
            print(f"'{sub}' occurs {count_occurrences(text, sub)} time(s).")
        elif choice == "6":
            print("Without spaces:", remove_spaces(text))
        elif choice == "7":
            text = input("Enter a new string: ")
        elif choice == "8":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()