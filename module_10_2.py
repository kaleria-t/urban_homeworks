import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100
        self.days_counter = 0
    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            time.sleep(1)
            self.days_counter += 1
            self.enemy -= self.power
            print(f'{self.name} сражается {self.days_counter} дней, осталоcь {self.enemy} воинов')
            if self.enemy <= 0:
                print(f'{self.name} одержал победу спустя {self.days_counter} дней')
                
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()