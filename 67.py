# Validate user age with custom exceptions.

class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)


def validate_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    return "Age is valid. You are eligible."


try:
    age = int(input("Enter your age: "))
    result = validate_age(age)
    print(result)

except InvalidAgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input! Please enter a valid integer.")