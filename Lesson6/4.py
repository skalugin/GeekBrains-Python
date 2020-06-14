class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go to')

    def stop(self):
        print('Is stopping')

    def turn(self, direction):
        print(self.name, 'is turining to', direction)

    def show_speed(self):
        print ('Current speed is:', self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:  print('You exceed speed limit in:', self.speed - 60)

class Worker(Car):
    def show_speed(self):
        if self.speed > 40:  print('You exceed speed limit in:', self.speed - 40)

class PoliceCar(Car):
    pass
class SportCar(Car):
    pass

my_car = Worker(60, 'white', 'Tractor')
my_car.show_speed()
my_car.turn('right')