import logging


logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info("{} function has {} arguements".format(func.__name__,args))
        print("{} function has {} arguements".format(func.__name__,args))
        #logging.info(func(*args))
        print(func(*args))
    return log_func


def add(x,y):
    #print x+y
    return x+y

def sub(x,y):
    return x-y


if __name__ == '__main__':
    add_logger = logger(add)
    sub_logger = logger(sub)
    add_logger(2,3)
    sub_logger(3,2)


"""
As seen in the above example, closures are used to invoke functions outside their scope.
"""
