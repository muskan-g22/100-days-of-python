# Convert a sentence into title case without using .title().
sentence = input("Enter sentence: ")

words = sentence.split()

result = []

for word in words:
    result.append(word[0].upper() + word[1:].lower())

print(" ".join(result))