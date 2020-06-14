class Worker:
    def __init__(self, name, surname, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname

class Position(Worker):

    def get_full_name(self):
        print('Fulle name', self.name, self.surname)

    def get_total_income(self):
        print('Total salary:', self._income['wage'] + self._income['bonus'])
        pass

pos = Position('Sergey', 'Kalugin', 500, 100)
pos.get_full_name()
pos.get_total_income()

