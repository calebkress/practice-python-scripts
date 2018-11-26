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
