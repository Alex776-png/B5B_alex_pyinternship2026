employees = ["Dumperdink", "Mardenborough", "Salvador", "Fernando"]
salaries = [45000, 52000, 48000, 60000]

for name, salary in zip(employees, salaries):
    print(name, ":", salary)