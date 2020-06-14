class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        print ('Сумма клеток равна', self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            print('Разность клеток равна', self.count - other.count)
        else:
            print('Ошибка')

    def __mul__(self, other):
        print ('Умножение клеток равно', self.count * other.count)

    def __truediv__(self, other):
        if other.count !=0:
            print('Деление клеток равно', self.count // other.count)
        else:
            print('Ошибка')

    def make_order(self, row_count):
        return ('*' * row_count + '\n') * (self.count // row_count) + '*' * (self.count % row_count)



cell_1 = Cell(2)
cell_2 = Cell(0)

cell_1 + cell_2
cell_1 - cell_2

cell_1 / cell_2

cell_1.count = 12
print(cell_1.make_order(5))

