# 74	Copy contents from one file to another.
with open("user_data.txt", "r") as source:
    content = source.read()

with open("destination.txt", "w") as destination:
    destination.write(content)

print("File copied successfully!")