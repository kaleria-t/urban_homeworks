class Figure:
    filled = False # закрашенный

    def __init__(self, colors_, side_, *, sides_count):
        self.__color = colors_
        self.side_ = side_
        self.sides_count = sides_count
        self.make_sides_list()

    def make_sides_list(self):
        for i in range(self.sides_count):
            self.__sides = []
            self.__sides.append(self.side_)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int): # 2 раза запускается проверка??
        self.color_is_valid = False
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            #print('isinstance')
            if 0<=r<=255:
                if 0<=g<=255:
                    if 0<=b<=255:
                        self.color_is_valid = True # работает
                        #print('True, 1') # работает
        return self.color_is_valid

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            #print ('Результат проверки __is_valid_color():', self.__is_valid_color(r, g, b))
            self.__color = [r, g, b]
            #print('Цвет успешно выбран в set_color()')
        else:
            print('Результат проверки __is_valid_color:', self.__is_valid_color(r, g, b))
        return self.__color

    def __is_valid_sides(self, *args):
        if self.sides_count == len(args):
            for i in args:
                if i > 0 and isinstance(i, int):
                    a = True
                else:
                    return False
            return a
        else:
            return False
            #возвращает True если все стороны целые положительные числа и кол-во новых сторон
            # совпадает с текущим(переданным из класса фигуры sides_count), False - во всех остальных случаях.

    def get_sides(self):
        return self.__sides

    def get_1_side(self): # for cube and circle
        return self.__sides[0]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            if self.sides_count == len(new_sides):
                self.__sides = []
                for i in new_sides:
                    self.__sides.append(i)
        self.side_ = self.__sides[0]
        return self.__sides


    def __len__(self):
        self.perimeter = sum(self.__sides)
        return self.perimeter

class Circle(Figure):

    def __init__(self, colors_, side_):
        self.sides_count = 1
        super().__init__(colors_, side_, sides_count=self.sides_count)

    def get_radius(self):
        self.__radius = self.get_1_side() / (2 * 3.14)
        return self.__radius

    def get_square(self):
        circle_square = 3.14*(self.__radius**2)
        return circle_square

class Triangle(Figure):

    def __init__(self, colors_, *sides_):
        self.sides_count = 3
        super().__init__(colors_, sides_, sides_count=self.sides_count)

    def triangle_sides(self):
        lst_ = self.get_sides()
        self.a = lst_[0][0]
        self.b = lst_[0][1]
        self.c = lst_[0][2]

    def get_square(self):
        self.triangle_sides()
        p = 0.5 * (self.a + self.b +self.c)
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s

class Cube(Figure):

    def __init__(self, colors_, *sides_: int):
        self.sides_count = 12
        super().__init__(colors_, *sides_, sides_count=self.sides_count)
        if len(sides_) == 1:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(*sides_)
        self.cube_side = self.__sides[0]

    def get_volume(self):
        v = self.cube_side ** 3
        return v

    def get_sides(self):
        return self.__sides


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

