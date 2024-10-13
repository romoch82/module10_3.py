import time
import random
import threading
from threading import Lock

class Bank:

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            random_int = random.randint(50, 500)
            self.balance += random_int
            print(f'Пополнение: {random_int}. Баланс: {self.balance}')
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            random_int = random.randint(50, 500)
            print(f'Запрос на {random_int}.')
            if random_int <= self.balance:
                self.balance -= random_int
                print(f'Снятие: {random_int}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')