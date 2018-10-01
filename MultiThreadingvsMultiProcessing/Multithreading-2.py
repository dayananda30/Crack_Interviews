import time
import threading

def calc_square(nums):
    print("Printing the Sqaures of {} ".format(nums))
    print("*"*40)
    for num in nums:
        time.sleep(0.2)
        print("The Square of {} is {}".format(num,num*num))

def calc_cube(nums):
    print("Printing the cubes of {}".format(nums))
    print("*"*40)
    for num in nums:
        time.sleep(0.2)
        print("The Cube of {} is {}".format(num,num*num*num))

if __name__=='__main__':
    print("This program to Demonstarate program with multithreading")
    print("#"*60)
    numbers = [1,2,3,4,5]
    start_time = time.time()
    t1 = threading.Thread(target=calc_square, args=(numbers,))#calc_square(numbers)
    t2 = threading.Thread(target=calc_cube, args=(numbers,))#calc_cube(numbers)

    t1.start()
    t2.start()

    t1.join()  # Wait till t1 is Done
    t2.join()   # Wait till t2 is Done

    total_time = time.time() - start_time
    print("The Total Time it took is : {} Seconds".format(total_time))
