# 80	Build a Contact Book (Add, Delete, Search Contact).
contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully!")

    # Delete Contact
    elif choice == "2":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Search Contact
    elif choice == "3":
        name = input("Enter contact name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    # Display Contacts
    elif choice == "4":
        if len(contacts) == 0:
            print("Contact book is empty!")
        else:
            print("\n--- All Contacts ---")
            for name, phone in contacts.items():
                print(f"Name: {name} | Phone: {phone}")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")