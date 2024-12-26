import threading
import random
import time
lock = threading.Lock()
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        counter = 100
        lock.acquire()
        while counter:
            counter -= 1
            self.balance += (a:=random.randint(50, 500))
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            if lock.locked() and self.balance >= 500:
                    lock.release()
            time.sleep(0.001)
        lock.release()
    def take(self):
        count = 100
        while count:
            print(f'Запрос на {(b:=random.randint(50, 500))}')
            if b <= self.balance:
                self.balance -= b
                print (f'Снятие: {b}. Баланс: {self.balance}')
            if b > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')