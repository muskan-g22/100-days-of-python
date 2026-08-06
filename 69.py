# Handle file-not-found exceptions.
filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        print("\nContents of the file:\n")
        print(file.read())

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")