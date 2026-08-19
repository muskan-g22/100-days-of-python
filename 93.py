# 93	Perform CRUD operations on SQLite records.
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    marks REAL
)
""")

# CREATE - Insert record
def add_student(name, age, marks):
    cursor.execute(
        "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
        (name, age, marks)
    )
    conn.commit()
    print("Student added successfully!")


# READ - Display records
def show_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        print(student)


# UPDATE - Update record
def update_student(student_id, name, age, marks):
    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, marks = ?
        WHERE id = ?
    """, (name, age, marks, student_id))

    conn.commit()
    print("Student updated successfully!")


# DELETE - Delete record
def delete_student(student_id):
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    print("Student deleted successfully!")


# Example usage
add_student("Muskan", 20, 85)
add_student("Manjeet", 21, 90)

print("\nAll Students:")
show_students()

update_student(1, "Muskan Sharma", 20, 92)

print("\nAfter Update:")
show_students()

delete_student(2)

print("\nAfter Delete:")
show_students()

# Close connection
conn.close()