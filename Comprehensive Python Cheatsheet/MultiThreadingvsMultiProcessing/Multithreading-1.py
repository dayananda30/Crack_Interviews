import time

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
    print("This program to Demonstarate program without multithreading")
    print("#"*60)
    numbers = [1,2,3,4,5]
    start_time = time.time()
    calc_square(numbers)
    calc_cube(numbers)
    total_time = time.time() - start_time
    print("The Total Time it took is : {} Seconds".format(total_time))
