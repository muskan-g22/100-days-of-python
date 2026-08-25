# Accept a password and check whether it satisfies:
# Minimum length
# Uppercase
# Lowercase
# Digit
# Special character
# Display Weak, Medium, or Strong.

import re

def check_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[@$!%*?&#]', password))

    # Calculate total criteria met
    passed_criteria = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_criteria
    ])

    # Determine strength rating
    if passed_criteria == 5:
        strength = "Strong"
    elif passed_criteria >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, {
        "Minimum length (>=8)": length_criteria,
        "Uppercase letter": uppercase_criteria,
        "Lowercase letter": lowercase_criteria,
        "Digit": digit_criteria,
        "Special character (@$!%*?&)": special_criteria
    }


user_password = input("Enter a password to check: ")
rating, breakdown = check_password_strength(user_password)

print(f"\nPassword Strength: {rating}")
print("Breakdown:")
for rule, passed in breakdown.items():
    status = "✓" if passed else "✗"
    print(f"  [{status}] {rule}")