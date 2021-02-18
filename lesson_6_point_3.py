class Worker:

    def __init__(self, name, sur_name, position, wage, bonus):
        self.name = name
        self.sur_name = sur_name
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, sur_name, position, wage, bonus):
        super().__init__(name, sur_name, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.sur_name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


x = Position('Stanislav', 'Musatov', 'middle', 100000, 60000)
print(x.get_full_name())
print(x.position)
print(x.get_total_income())