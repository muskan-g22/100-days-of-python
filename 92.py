# 92	Insert student records into SQLite.
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    marks REAL
)
""")

# Insert student records
students = [
    ("Muskan", 20, 85.5),
    ("Rahul", 21, 78.0),
    ("Priya", 20, 91.5),
    ("Aman", 22, 74.0)
]

cursor.executemany("""
INSERT INTO students (name, age, marks)
VALUES (?, ?, ?)
""", students)

# Save changes
conn.commit()

print("Student records inserted successfully!")

# Close connection
conn.close()