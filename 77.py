# 77	Read CSV data and calculate average marks.
import csv

total = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = float(row["Marks"])
        total += marks
        count += 1

average = total / count

print("Average Marks:", average)