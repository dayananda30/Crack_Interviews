"""
Create Two Processes:
1.  To calculate square of all numbers.
2.  To calculate cube of all numbers.
"""

import time
import multiprocessing


def calc_square(nums):
    for num in nums:
        time.sleep(0.2)
        print("The square of {} is {} ".format(num,num*num))

def calc_cube(nums):
    for num in nums:
        time.sleep(0.2)
        print("The Cube of {} is {}".format(num,num*num*num))


if __name__ == '__main__':
    print("Demonstrating MultiProcessing")
    start_time = time.time()
    numbers = [1,2,3,4,5]
    p1 = multiprocessing.Process(target=calc_square, args=(numbers,)) #calc_square(numbers)
    p2 = multiprocessing.Process(target=calc_cube, args=(numbers,))   #calc_cube(numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("The Total time it took to execute is {}".format(time.time()-start_time))
