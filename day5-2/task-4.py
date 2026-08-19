class Bird:
    def fly(self):
        print("Bird is flying by flapping its wings.")


class Airplane:
    def fly(self):
        print("Airplane is flying using its engines.")


class Drone:
    def fly(self):
        print("Drone is flying using its propellers.")


def make_it_fly(obj):
    obj.fly()


bird = Bird()
airplane = Airplane()
drone = Drone()

make_it_fly(bird)
make_it_fly(airplane)
make_it_fly(drone)