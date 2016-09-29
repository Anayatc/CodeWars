class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        x = 'This is a %s %s with %d MPG.' % (self.color, self.model, self.mpg)
        return x

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = 'like new'


my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition