import functools
import time

def timer(func):
    """ Print the runtime of the Decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args,**kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print("Finished {} in {} Seconds".format(func.__name__,run_time))
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(100000)])


if __name__ == '__main__':
    waste_some_time(9)
