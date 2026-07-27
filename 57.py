# Store student marks in a dictionary and find the topper.


students = {}

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# Find the topper
topper = max(students, key=students.get)

print("\nStudent Marks:")
for name, marks in students.items():
    print(name, ":", marks)

print("\nTopper:", topper)
print("Marks:", students[topper])