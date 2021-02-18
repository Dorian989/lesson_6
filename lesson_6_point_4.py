class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name}  start'

    def stop(self):
        return f'{self.name}  stop'

    def turn_right(self):
        return f'{self.name}  turn right'

    def turn_left(self):
        return f'{self.name}  turn left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
                super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police statment'

    def show_speed(self):
        print(f'speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} speed is higher then allow'

    def show_speed(self):
        print(f'speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} speed is higher then allow'


ferrary = SportCar(200, 'Red', 'ferrary', False)
priora = TownCar(35, 'Brown', 'Priora', False)
lada = WorkCar(80, 'Green', 'Lada', True)
volksvagen = PoliceCar(110, 'Blue',  'Ford', True)

print(lada.turn_left())
print(f'{lada.go()} with speed exactly {lada.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(ferrary.show_speed())
print(volksvagen .police())
print(volksvagen .show_speed())