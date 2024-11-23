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
        products_ = file.read()
        file.close()
        return products_

    def add(self, *products):
        current_products = self.get_products()
        file_ = open(self.__file_name, 'a')
        for i in products:
            if str(i) not in current_products:
                file_.write(str(i)) # ValueError: I/O operation on closed file. - при первых двух запусках,
                # с третьего запуска ошибки нет
                file_.close()
            if i.name in current_products:
                print(f'Продукт {i.name}, {i.weight}, {i.category} уже есть в магазине')








s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())