# Dog class with the ability to wag tail and increase happiness level
class Dog():
    def __init__(self, name='Dog', happiness_level=5):
        self.name = name
        self.happiness_level = happiness_level

    def wag_tail(self, num):
        print('{} wags its tail {} times.').format(self.name, num)
        self.happiness_level += (num * 5)
        print('{}\'s happiness level is now {}').format(self.name, self.happiness_level)

dog = Dog()
dog.wag_tail(3)

# Cat class with ability to sense an earthquake and run away
class Cat():
    def __init__(self, name='Cat', laziness_level='5', location='home'):
        self.name = name
        self.laziness_level = laziness_level
        self.location = location

    def sense_earthquake(self, earthquake):
        if earthquake == True:
            self.location = 'gone dark'
            print(self.location)

cat = Cat()
cat.sense_earthquake(True)

# Car class with the ability to drive and track gas levels
class Car():
    def __init__(self, model = 'Camry', color = 'grey', tank_size = 20):
        self.model = model
        self.color = color
        self.tank_size = tank_size
        self.gallons_of_gas = self.tank_size

    def drive(self, miles_driven):
        self.gallons_of_gas -= (miles_driven / 10)

car = Car()
print('The car has {} gallons left in the tank.').format(car.gallons_of_gas)
car.drive(150)
print('The car has {} gallons left in the tank.').format(car.gallons_of_gas)

# Plane class with the ability to fly between destinations
class Plane():
    def __init__(self, destination='Edinburgh', departure_city='Austin', trip_distance=4676):
        self.destination = destination
        self.departure_city = departure_city
        self.trip_distance = trip_distance

    def fly(self):
        self.departure_city, self.destination = self.destination, self.departure_city

plane = Plane()
print('in ' + plane.departure_city, 'heading to ' + plane.destination)
plane.fly()
print('Flying')
print('in ' + plane.departure_city, 'heading to ' + plane.destination)
