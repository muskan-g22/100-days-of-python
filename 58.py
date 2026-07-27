# Count the occurrence of each word in a paragraph.

paragraph = input("Enter a paragraph: ")

# Convert to lowercase and split into words
words = paragraph.lower().split()

word_count = {}

for word in words:
    # Remove common punctuation
    word = word.strip(".,!?;:'\"()[]{}")

    if word:
        word_count[word] = word_count.get(word, 0) + 1

print("\nWord Occurrences:")
for word, count in word_count.items():
    print(f"{word} : {count}")