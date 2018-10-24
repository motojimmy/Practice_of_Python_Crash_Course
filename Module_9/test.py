class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def descriptive_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

my_besla = ElectricCar('tesla', 'model s', 2016)
print(my_besla.get_descriptive_name())
my_besla.descriptive_battery()

