# Find the longest word in a sentence.
sentence = "Python is an amazing programming language"

# Step 1: Split the sentence into individual words
words = sentence.split()

# Step 2: Set the first word as the baseline
longest_word = words[0]

# Step 3: Compare each word's length against the current longest word
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"The longest word is: '{longest_word}'")
