# 85	Create a Student class with marks and grade calculation.
class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    # Calculate Grade
    def get_grade(self):

        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    # Check Pass/Fail
    def is_passed(self):

        return self.marks >= 50

    # Display Student
    def display(self):

        print("\n----------------------------")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Grade:", self.get_grade())
        print(
            "Status:",
            "Passed" if self.is_passed() else "Failed"
        )


students = {}


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

    student = Student(
        student_id,
        name,
        age,
        course,
        marks
    )

    students[student_id] = student

    print("Student added successfully!")


# View All Students
def view_students():

    if not students:
        print("No students found.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students.values():
        student.display()


# Search Student
def search_student():

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    students[student_id].display()


# Update Student
def update_student():

    student_id = input("Enter Student ID: ")

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

        student.name = input("Enter new name: ")

    elif choice == "2":

        student.age = int(
            input("Enter new age: ")
        )

    elif choice == "3":

        student.course = input(
            "Enter new course: "
        )

    elif choice == "4":

        marks = float(
            input("Enter new marks: ")
        )

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student.marks = marks

    else:

        print("Invalid choice!")
        return

    print("Student updated successfully!")


# Delete Student
def delete_student():

    student_id = input("Enter Student ID: ")

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

    topper = max(
        students.values(),
        key=lambda student: student.marks
    )

    print("\n========== TOPPER ==========")

    topper.display()


# Display Passed Students
def passed_students():

    found = False

    print("\n========== PASSED STUDENTS ==========")

    for student in students.values():

        if student.is_passed():

            student.display()
            found = True

    if not found:
        print("No student has passed.")


# Display Failed Students
def failed_students():

    found = False

    print("\n========== FAILED STUDENTS ==========")

    for student in students.values():

        if not student.is_passed():

            student.display()
            found = True

    if not found:
        print("No student has failed.")


# Main Program

while True:

    print("\n====================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. View Passed Students")
    print("8. View Failed Students")
    print("9. Exit")

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
        passed_students()

    elif choice == "8":
        failed_students()

    elif choice == "9":

        print(
            "Thank you for using "
            "Student Management System!"
        )

        break

    else:
        print("Invalid choice!")