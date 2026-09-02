# Store student names and marks using lists. Display topper, average, lowest marks, and search for a student.

def student_marks_manager():
    names = []
    marks = []

    # Input student data
    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        name = input(f"Enter name of student {i + 1}: ").strip()
        mark = float(input(f"Enter marks for {name}: "))
        names.append(name)
        marks.append(mark)

    if not marks:
        print("\nNo student records found.")
        return

    # Calculate statistics
    avg_marks = sum(marks) / len(marks)
    max_marks = max(marks)
    min_marks = min(marks)

    # Find topper(s) and lowest scorer(s)
    toppers = [names[i] for i in range(len(marks)) if marks[i] == max_marks]
    lowest_scorers = [names[i] for i in range(len(marks)) if marks[i] == min_marks]

    # Display results
    print("\n--- Class Performance ---")
    print(f"Average Marks: {avg_marks:.2f}")
    print(f"Top Score: {max_marks} (Student(s): {', '.join(toppers)})")
    print(f"Lowest Score: {min_marks} (Student(s): {', '.join(lowest_scorers)})")

    # Search functionality
    print("\n--- Search Student ---")
    search_name = input("Enter student name to search: ").strip()

    found = False
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"Result: {names[i]} scored {marks[i]} marks.")
            found = True
            break
            
    if not found:
        print(f"Result: Student '{search_name}' not found.")

# Run the program
student_marks_manager()