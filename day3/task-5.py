students=[("Riya", 88), ("Aman", 95), ("Sara", 72)]

students= list(students)

students=sorted(key=lambda student: student[1], reverse=True)

print('Sorted : ',students)