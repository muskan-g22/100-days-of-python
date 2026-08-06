# Create a custom exception for invalid marks.
class InvalidMarksError(Exception):
    """Raised when the entered marks fall outside the valid range (e.g., 0 to 100)."""
    
    def __init__(self, marks, message="Marks must be between 0 and 100"):
        self.marks = marks
        self.message = message
        super().__init__(f"{message} (Got: {marks})")
        
def validate_student_marks(marks):
    if not isinstance(marks, (int, float)):
        raise TypeError("Marks must be a number.")
    
    if marks < 0 or marks > 100:
        raise InvalidMarksError(marks)
    
    return f"Marks recorded: {marks}"


# --- Usage Example ---
test_scores = [85, 105, -10, "eighty"]

for score in test_scores:
    try:
        result = validate_student_marks(score)
        print(f"Success: {result}")
    except InvalidMarksError as e:
        print(f"Custom Exception Caught: {e}")
    except TypeError as e:
        print(f"Type Error: {e}")