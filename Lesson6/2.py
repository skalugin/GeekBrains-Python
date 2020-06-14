class Road:
    def __init__(self, length, width):
        self._mass = 25
        self.length = length
        self.width = width

    def get_mass(self):
        print('Weight: ', (self.length * self.width * 0.1 * self._mass))

r = Road(20, 5000)
r.get_mass()