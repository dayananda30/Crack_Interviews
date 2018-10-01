'''
Shared Memory

process 1 (Main process)  ------>     SHARED MEMORY   <--------    process 2 (child process (calc_square))

'''

import multiprocessing


def calc_square(numbers , result, v):
    v.value = 5.56
    for index,num in enumerate(numbers):
        result[index] = num*num


if __name__ == '__main__':
    number = [1,2,3]
    result = multiprocessing.Array('i',3)   #Result is the shared Array variable where "i" is to denote integer and 3 is the size
    v = multiprocessing.Value('d',0.0)
    p = multiprocessing.Process(target=calc_square, args=(number,result,v))

    p.start()

    p.join()

    print("The Result is : {}".format(result[:]))

    print("The Value is : {}".format(v.value))


