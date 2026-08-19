employees = {
    "Riya": 55000,
    "Aman": 75000,
    "Priya": 62000,
    "Rahul": 90000,
    "Neha": 80000,
    "Karan": 65000
}

sorted_employees = sorted(
    employees.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Top 3 highest paid employees:")

for name, salary in sorted_employees[:3]:
    print(name, salary)