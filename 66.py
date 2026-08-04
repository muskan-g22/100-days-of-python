# Handle division by zero using exception handling.
numerator = 10
denominator = 0

try:
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero.")
