'''
Using Queue as the Shared memory here

'''

import multiprocessing


def calc_square(numbers,q):
    for num in numbers:
        q.put(num*num)




if __name__=='__main__':
    number = [1,2,3,4,5,6]

    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=calc_square, args=(number,q))

    p.start()

    p.join()

    while q.empty() is False:
        print(q.get())

