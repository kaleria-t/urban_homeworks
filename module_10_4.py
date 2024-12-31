import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for i in guests:
            used_tables = 0
            for table in self.tables:
                if table.guest is None:
                    table.guest = i
                    i.start()
                    print(f"{i.name} сел(-а) за стол номер {table.number}")
                    break
                else:
                    used_tables += 1
            if used_tables == len(self.tables):
                self.queue.put(i)
                print(f"{i.name} в очереди")

    def discuss_guests(self):
        occupied_tables = False
        for t in self.tables:
            if t.guest is None:
                occupied_tables = False
            else:
                occupied_tables = True
                break
        while not self.queue.empty() or occupied_tables:
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive(): #гость был, поток завершён
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                    if not self.queue.empty(): #в очереди ещё есть гости
                        g = self.queue.get()
                        table.guest = g
                        print(f"{g.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        g.start()
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()