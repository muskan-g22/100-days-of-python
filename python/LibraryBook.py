# Library Book Tracker

# Maintain book records using dictionaries with search, issue, return, and availability status.
# Library Book Tracker

library = {
    "Python Basics": {
        "author": "John Smith",
        "available": True
    },
    "Data Structures": {
        "author": "Robert Martin",
        "available": True
    },
    "Django for Beginners": {
        "author": "William Green",
        "available": False
    },
    "Machine Learning": {
        "author": "Andrew Ng",
        "available": True
    }
}


def display_books():
    print("\n--- Library Books ---")

    for title, details in library.items():
        status = "Available" if details["available"] else "Issued"

        print(f"Book: {title}")
        print(f"Author: {details['author']}")
        print(f"Status: {status}")
        print("-" * 30)


def search_book():
    title = input("Enter book title to search: ")

    if title in library:
        details = library[title]

        status = "Available" if details["available"] else "Issued"

        print("\nBook Found!")
        print(f"Title: {title}")
        print(f"Author: {details['author']}")
        print(f"Status: {status}")
    else:
        print("Book not found.")


def issue_book():
    title = input("Enter book title to issue: ")

    if title not in library:
        print("Book not found.")
        return

    if library[title]["available"]:
        library[title]["available"] = False
        print(f"'{title}' has been issued successfully.")
    else:
        print(f"'{title}' is already issued.")


def return_book():
    title = input("Enter book title to return: ")

    if title not in library:
        print("Book not found.")
        return

    if not library[title]["available"]:
        library[title]["available"] = True
        print(f"'{title}' has been returned successfully.")
    else:
        print(f"'{title}' was not issued.")


while True:

    print("\n===== LIBRARY BOOK TRACKER =====")
    print("1. Display all books")
    print("2. Search book")
    print("3. Issue book")
    print("4. Return book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Thank you for using Library Book Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")