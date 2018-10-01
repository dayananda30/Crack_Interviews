"""

The global varibles used inside one process will not accessed by another process.

To know about this issue : please have a look into below code:

When below code is in execution , two process will be created with two address space for two different process respectively.
process 1 : Main program
process 2 : cal_square program.

problem:
--------
The global variable(result) used in calc_square has some value but if try to print same
global varibale in main process it returns [](NULL) since its address space is different.


Solution is : Shared Memory



URL: https://www.youtube.com/watch?v=uWbSc84he2Q&index=3&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN
"""


import multiprocessing

result=[]

def calc_square(nums):
    global result
    for num in nums:
        result.append(num*num)
    print("I'm Inside calc_square Process and the result is : {} ".format(str(result)))


if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    p = multiprocessing.Process(target=calc_square, args=(numbers,))

    p.start()

    p.join()

    print("I'm outside of calc_square process and inside main process. The value of result is : {}".format(str(result)))
