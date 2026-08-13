# 82	Create a Library Management System.
books = {}


# Add Book
def add_book():
    book_id = input("Enter Book ID: ")

    if book_id in books:
        print("Book ID already exists!")
        return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    category = input("Enter Category: ")

    books[book_id] = {
        "name": name,
        "author": author,
        "category": category,
        "available": True,
        "issued_to": None
    }

    print("Book added successfully!")


# View All Books
def view_books():
    if not books:
        print("No books available.")
        return

    print("\n========== ALL BOOKS ==========")

    for book_id, book in books.items():
        print("\nBook ID:", book_id)
        print("Name:", book["name"])
        print("Author:", book["author"])
        print("Category:", book["category"])

        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Issued")
            print("Issued To:", book["issued_to"])


# Search Book
def search_book():
    book_id = input("Enter Book ID to search: ")

    if book_id not in books:
        print("Book not found!")
        return

    book = books[book_id]

    print("\n========== BOOK DETAILS ==========")
    print("Book ID:", book_id)
    print("Name:", book["name"])
    print("Author:", book["author"])
    print("Category:", book["category"])

    if book["available"]:
        print("Status: Available")
    else:
        print("Status: Issued")
        print("Issued To:", book["issued_to"])


# Issue Book
def issue_book():
    book_id = input("Enter Book ID to issue: ")

    if book_id not in books:
        print("Book not found!")
        return

    book = books[book_id]

    if not book["available"]:
        print("Book is already issued!")
        return

    student = input("Enter Student Name: ")

    book["available"] = False
    book["issued_to"] = student

    print("Book issued successfully!")


# Return Book
def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id not in books:
        print("Book not found!")
        return

    book = books[book_id]

    if book["available"]:
        print("This book is already available in the library.")
        return

    book["available"] = True
    book["issued_to"] = None

    print("Book returned successfully!")


# Delete Book
def delete_book():
    book_id = input("Enter Book ID to delete: ")

    if book_id not in books:
        print("Book not found!")
        return

    if not books[book_id]["available"]:
        print("Cannot delete an issued book!")
        return

    del books[book_id]

    print("Book deleted successfully!")


# View Issued Books
def issued_books():
    found = False

    print("\n========== ISSUED BOOKS ==========")

    for book_id, book in books.items():

        if not book["available"]:
            found = True

            print("\nBook ID:", book_id)
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Issued To:", book["issued_to"])

    if not found:
        print("No books are currently issued.")


# Main Program
while True:

    print("\n===================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        issued_books()

    elif choice == "8":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")