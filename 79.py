
# Simple Notes Application using File Handling

FILE_NAME = "notes.txt"


def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note added successfully!")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes found.")
        else:
            print("\n--- Your Notes ---")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")

    except FileNotFoundError:
        print("No notes found.")


def search_note():
    keyword = input("Enter keyword to search: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        found = False

        for i, note in enumerate(notes, start=1):
            if keyword in note.lower():
                print(f"{i}. {note.strip()}")
                found = True

        if not found:
            print("No matching note found.")

    except FileNotFoundError:
        print("No notes found.")


def delete_notes():
    open(FILE_NAME, "w").close()
    print("All notes deleted successfully!")


while True:
    print("\n===== NOTES APPLICATION =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Delete All Notes")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        search_note()

    elif choice == "4":
        delete_notes()

    elif choice == "5":
        print("Thank you for using Notes Application!")
        break

    else:
        print("Invalid choice!")