# Write user data into a text file.
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

with open("user_data.txt", "w") as file:
    file.write("User Data\n")
    file.write("---------\n")
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Email: {email}\n")

print("User data saved successfully!")