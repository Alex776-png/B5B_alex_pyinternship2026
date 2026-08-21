class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= self.__salary:
            self.__salary = new_salary
        else:
            print("Invalid: Salary cannot be decreased.")


employee = Employee(50000)

print("Original salary:", employee.get_salary())

employee.set_salary(60000) #valid
print("After increase:", employee.get_salary())

employee.set_salary(40000) #invalid
print("After decrease attempt:", employee.get_salary())