# Create a safe calculator using try-except.
try:
    expression = input("Enter expression (e.g., 10 + 5): ")
    result = eval(expression)
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except SyntaxError:
    print("Error: Invalid expression.")

except NameError:
    print("Error: Invalid input. Enter only numbers and operators.")

except Exception as e:
    print("Error:", e)