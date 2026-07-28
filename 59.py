# Create a phone book using a dictionary.
# Create a phone book using a dictionary

phone_book = {}

n = int(input("Enter the number of contacts: "))

for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phone_book[name] = phone

print("\nPhone Book:")
for name, phone in phone_book.items():
    print(name, ":", phone)

# Search for a contact
search = input("\nEnter the name to search: ")

if search in phone_book:
    print("Phone Number:", phone_book[search])
else:
    print("Contact not found.")