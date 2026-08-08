# 75	Search a word inside a file.
word = input("Enter the word to search: ")

with open("user_data.txt", "r") as file:
    content = file.read()

if word in content:
    print("Word found!")
else:
    print("Word not found!")