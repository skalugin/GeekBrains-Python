class Clothes:
    def __init__(self):
        self. title = ''

class Coat(Clothes):
    def __init__(self, value):
        self.value = value
        self.title = 'Пальто'

    @property
    def consumption(self):
        #return 'Для', self.title, 'необходимо ', str(self.value / 6.5 + 0.5), 'ткани'
        return int(self.value / 6.5 + 0.5)

class Suit(Clothes):
    def __init__(self, heigh):
        self.title = 'Костюм'
        self.heigh = heigh
    @property
    def consumption(self):
        #return 'Для', self.title,'необходимо ', str(self.heigh *2 + 0.3), 'ткани'
        return int(self.heigh * 2 + 0.3)

my_coat = Coat(5)
print(my_coat.consumption)

my_suit = Suit(3)
print(my_suit.consumption)