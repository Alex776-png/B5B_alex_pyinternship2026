class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C.")
        self.__celsius = value

    @property
    def kelvin(self):
        return self.celsius + 273.15


temperature = Temperature(25)

print("Celsius:", temperature.celsius)
print("Kelvin:", temperature.kelvin)

try:
    temperature.celsius = -300
except ValueError as e:
    print("Error:", e)