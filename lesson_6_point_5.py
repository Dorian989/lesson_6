class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f' Lunch draw {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f' {self.title}. lunch draw pen'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f' {self.title}. lunch draw pencil'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f' {self.title}. lunch draw handle'

pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

print(pen.draw())
print(pencil.draw())
print(handle.draw())