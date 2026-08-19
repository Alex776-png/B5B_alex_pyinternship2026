class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def show_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Top Speed:", self.top_speed, "km/h")


sports_car = SportsCar("Ferrari", "488 GTB", 330)

sports_car.show_info()