class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")


student = Student("Rahul", 20, "Computer Science")

print(student.name)
print(student.age)
print(student.course)
student.study()