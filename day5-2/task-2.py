class Employee:
    def calculate_salary(self):
        return 50000


class Developer(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        bonus = 10000
        return base_salary + bonus


class Designer(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        bonus = 8000
        return base_salary + bonus


developer = Developer()
designer = Designer()

print("Developer salary :", developer.calculate_salary())
print("Designer salary :", designer.calculate_salary())