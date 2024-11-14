class Vehicle:

    __COLOR_VARIANTS = ['black', 'light_grey', 'grey', 'white']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return 'Мощность двигателя', self.__engine_power

    def get_color (self):
        return 'Цвет', self.__color

    def print_info(self):
        print(self.get_model, self.get_horsepower, self.get_color, 'Владелец:', self.owner)

    def set_color(self, new_color):
        lst = []
        for x in self.__COLOR_VARIANTS:
            lst.append(x.lower)
        for i in lst:
            if new_color.lower == i:
                self.__color = new_color
                print('Новый цвет:', self.__color)
        else:
                print ('Нельзя сменить цвет на', new_color)

    def __str__(self):
        return str(self.get_model), str(self.get_horsepower), str(self.get_color), str(self.owner)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

