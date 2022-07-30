'''
The ideal Output should be 200 but if you execute this program more times it behaves
differently and giving output differently at each call.

due to asyncheronous calls


'''


import multiprocessing
import time

def deposit(balance, deposit_amt):
    for rupees in range(100):
        time.sleep(0.01)
        balance.value = balance.value + rupees


def withdraw(balance, withdraw_amt):
    for rupees in range(100):
        time.sleep(0.01)
        balance.value = balance.value - rupees




if __name__=='__main__':
    balance = multiprocessing.Value('i',200)
    deposit_amt = multiprocessing.Value('i',100)
    deposit_process = multiprocessing.Process(target=deposit, args=(balance,deposit_amt))

    withdraw_amt = multiprocessing.Value('i',100)
    withdraw_process = multiprocessing.Process(target=withdraw, args=(balance,withdraw_amt))

    deposit_process.start()
    withdraw_process.start()

    deposit_process.join()
    withdraw_process.join()


    print("The balance is : {} ".format(balance.value))



