# Remove duplicate characters from a string.

str = input("Enter string ")
result =""
seen = set()
for char in str:
    if char not in seen:
        seen.add(char)
        result +=char

print(result)