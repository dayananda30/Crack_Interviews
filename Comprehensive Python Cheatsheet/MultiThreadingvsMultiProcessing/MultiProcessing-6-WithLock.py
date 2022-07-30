import multiprocessing
import time

def deposit(balance, lock):
    for rupees in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + rupees #CRITICAL SECTION
        lock.release()


def withdraw(balance, lock):
    for rupees in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - rupees
        lock.release()


if __name__=='__main__':
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    deposit_process = multiprocessing.Process(target=deposit, args=(balance,lock))
    withdraw_process = multiprocessing.Process(target=withdraw, args=(balance,lock))

    deposit_process.start()
    withdraw_process.start()

    deposit_process.join()
    withdraw_process.join()


    print("The balance is : {} ".format(balance.value))
