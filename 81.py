# 81	Create a Student Management System.
students = {}


# Calculate Grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# Add Student
def add_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


# View All Students
def view_students():
    if not students:
        print("No students found.")
        return

    print("\n===== ALL STUDENTS =====")

    for student_id, student in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("Grade:", calculate_grade(student["marks"]))


# Search Student
def search_student():
    student_id = input("Enter Student ID to search: ")

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("\n===== STUDENT DETAILS =====")
    print("Student ID:", student_id)
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("Marks:", student["marks"])
    print("Grade:", calculate_grade(student["marks"]))


# Update Student
def update_student():
    student_id = input("Enter Student ID to update: ")

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("\n1. Update Name")
    print("2. Update Age")
    print("3. Update Course")
    print("4. Update Marks")

    choice = input("Enter your choice: ")

    if choice == "1":
        student["name"] = input("Enter new name: ")

    elif choice == "2":
        student["age"] = int(input("Enter new age: "))

    elif choice == "3":
        student["course"] = input("Enter new course: ")

    elif choice == "4":
        marks = float(input("Enter new marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student["marks"] = marks

    else:
        print("Invalid choice!")
        return

    print("Student updated successfully!")


# Delete Student
def delete_student():
    student_id = input("Enter Student ID to delete: ")

    if student_id not in students:
        print("Student not found!")
        return

    del students[student_id]

    print("Student deleted successfully!")


# Find Topper
def find_topper():
    if not students:
        print("No students found.")
        return

    topper_id = max(
        students,
        key=lambda student_id: students[student_id]["marks"]
    )

    topper = students[topper_id]

    print("\n===== TOPPER =====")
    print("Student ID:", topper_id)
    print("Name:", topper["name"])
    print("Course:", topper["course"])
    print("Marks:", topper["marks"])
    print("Grade:", calculate_grade(topper["marks"]))


# Main Program
while True:

    print("\n================================")
    print("    STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        find_topper()

    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")