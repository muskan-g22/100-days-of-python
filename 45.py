# Create a simple password validator.
password = input('''Enter password 
Conditions:
* Minimum 8 characters
* One uppercase
* One lowercase
* One digit 
    : ''')

upper = False
lower = False
digit = False

for ch in password:

    if ch.isupper():
        upper = True

    elif ch.islower():
        lower = True

    elif ch.isdigit():
        digit = True

if len(password) >= 8 and upper and lower and digit:
    print("Valid")

else:
    print("Invalid")