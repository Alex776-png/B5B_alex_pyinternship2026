students = [
    {"name": "Riya", "marks": 88},
    {"name": "Aman", "marks": 95},
    {"name": "Priya", "marks": 91},
    {"name": "Rahul", "marks": 87}
]

highest_student = students[0]

for student in students:
    if student["marks"] > highest_student["marks"]:
        highest_student = student

print("Student with highest marks:", highest_student["name"])
print("Marks:", highest_student["marks"])