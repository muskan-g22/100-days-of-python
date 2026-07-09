
# Python program to count words, characters, and spaces

sentence = input("Enter a sentence: ")

characters = 0
spaces = 0
words = 0
in_word = False

for ch in sentence:
    characters += 1

    if ch == ' ':
        spaces += 1
        in_word = False
    else:
        if in_word == False:
            words += 1
            in_word = True

print("Number of characters:", characters)
print("Number of spaces:", spaces)
print("Number of words:", words)