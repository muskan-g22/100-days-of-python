# 78	Store and retrieve data using JSON.
import json

# Student data
student = {
    "roll_no": 101,
    "name": "Muskan",
    "age": 21,
    "marks": 85
}

# Store data in JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data stored successfully!")

# Retrieve data from JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print("\nRetrieved Data:")
print("Roll No:", data["roll_no"])
print("Name:", data["name"])
print("Age:", data["age"])
print("Marks:", data["marks"])