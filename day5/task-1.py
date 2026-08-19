class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model}.")


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Ford", "Mustang", 2024)

car1.display_info()
car2.display_info()
car3.display_info()