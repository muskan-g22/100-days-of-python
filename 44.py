# Replace all vowels with * in a string.
str= input("Enter string : ")
result=''
for char in str:
    if char in "AEIOUaeiou":
        result += "*"
    else:
        result+=char

print(result)