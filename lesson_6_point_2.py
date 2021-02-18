class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

class MassCount(Road):
    def __init__(self, _length, _width, vol):
        super().__init__(_length, _width)
        self.volume = vol

m = MassCount(25, 100000, 125)
print(m.mass())
