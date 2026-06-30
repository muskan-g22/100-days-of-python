#Create a function to reverse a string without slicing.
def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))