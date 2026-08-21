students = [
    {"name": "Fragile", "marks": 88},
    {"name": "Christopher", "marks": 95},
    {"name": "Alucard", "marks": 91},
    {"name": "Norington", "marks": 87}
]

highest_student = students[0]

for student in students:
    if student["marks"] > highest_student["marks"]:
        highest_student = student

print("Student with highest marks :", highest_student["name"])
print("Marks :", highest_student["marks"])