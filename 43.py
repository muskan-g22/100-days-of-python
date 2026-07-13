# Check whether a string is a palindrome.
str= input("Enter string : ")
if str == str[::-1]:
    print("String is palindrom")
else:
    print("Not a palindrom ") 