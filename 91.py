# 91	Create a SQLite database and student table.
import sqlite3

# Connect to database
connection = sqlite3.connect("students.db")

# Create cursor
cursor = connection.cursor()

# Create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")

# Save changes
connection.commit()

print("Database and Student table created successfully!")

# Close connection
connection.close()