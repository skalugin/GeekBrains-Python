class Stationery:

    def __init__(self, ):
        self.title = "родителский класс"

    def draw(self):
        print('Запуск отрисовки в родительском классе')

class Pen(Stationery):
    def draw(self):
        print('Рисуем карандашем')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем ручкой')

class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


my_pen = Pen()
my_pen.draw()
my_pencil = Pencil()
my_pencil.draw()
my_handle = Handle()
my_handle.draw()
