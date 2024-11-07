class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        House.houses_history.append(args)
        return super().__new__(cls)
    def __init__(self, name, count_floors):
        self.name = name
        self.number_of_floors = count_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return str(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        self.number_of_floors += value
        return self
    def __radd__(self, value):
        self.__add__(value)
        return self
    def __iadd__(self, value):
        self.__add__(value)
        return self
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)

#print(h1)
#print(h2)
#print(h1 == h2) # __eq__
#h1 = h1 + 10 # __add__
#print(h1)
#print(h1 == h2)
#h1 += 10 # __iadd__
#print(h1)
#h2 = 10 + h2 # __radd__
#print(h2)
#print(h1 > h2) # __gt__
#print(h1 >= h2) # __ge__
#print(h1 < h2) # __lt__
#print(h1 <= h2) # __le__
#print(h1 != h2) # __ne__

