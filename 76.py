# 76	Store student records in a CSV file.
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Roll No", "Name", "Age", "Marks"])

    # Student records
    writer.writerow([101, "Muskan", 21, 85])
    writer.writerow([102, "Rahul", 20, 90])
    writer.writerow([103, "Priya", 21, 78])

print("Student records saved successfully!")