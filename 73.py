# Count lines, words, and characters in a file.
with open("user_data.txt", "r") as file:
    lines = 0
    words = 0
    characters = 0

    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)

print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)

