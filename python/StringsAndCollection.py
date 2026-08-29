
# Analyze a sentence and display:

# Total words
# Total characters
# Vowels
# Consonants
# Digits
# Special symbols

def analyze_sentence(sentence):
    vowels_set = set("aeiouAEIOU")

    words = sentence.split()
    total_words = len(words)
    total_chars = len(sentence)
    vowels = sum(1 for char in sentence if char in vowels_set)
    consonants = sum(
        1 for char in sentence if char.isalpha() and char not in vowels_set
    )
    digits = sum(1 for char in sentence if char.isdigit())
    special_symbols = sum(
        1 for char in sentence if not char.isalnum() and not char.isspace()
    )

    print(f"Total words: {total_words}")
    print(f"Total characters: {total_chars}")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")
    print(f"Special symbols: {special_symbols}")


# Example Usage
text = input("Enter a sentence: ")
analyze_sentence(text)