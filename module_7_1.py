from pprint import pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(self.__file_name.read())
        file.close()

    def add(self, *products):
        for i in products:
            if i not in str('products.txt'): # TypeError: 'in <string>' requires string as left operand, not Product 
                file_ = open(self.__file_name, 'a')
                file_.write(i)
                file_.close()
            if i in self.__file_name:
                print(f'Продукт {i.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
