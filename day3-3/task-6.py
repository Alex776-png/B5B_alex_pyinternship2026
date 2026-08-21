employees = {
    "Alice": 55000,
    "Norington": 75000,
    "Paul": 62000,
    "Fernando": 90000,
    "Gonsalvis": 80000,
    "Yeager": 65000
}

sorted_employees = sorted(employees.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Top 3 highest paid employees:")

for name, salary in sorted_employees[:3]:
    print(name, salary)