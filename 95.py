import re

def validate_mobile(number):
    pattern = r'^[6-9][0-9]{9}$'

    if re.match(pattern, number):
        print("Valid mobile number")
    else:
        print("Invalid mobile number")


number = input("Enter mobile number: ")
validate_mobile(number)