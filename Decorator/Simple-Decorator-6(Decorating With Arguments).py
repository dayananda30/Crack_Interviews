"""
Use *args and **kwargs in the inner wrapper function.
then it will accept an arbitrary number of positional and keyword arguments.

"""

def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function(*args, **kwargs):
    if args:
        print("Positional Args passed are  : {}".format(args))
    if kwargs:
        print("Variable Args passed are : ")
        for key in kwargs.keys():
            print("{} --> {}".format(key,kwargs[key]))

if __name__ == '__main__':
    my_function("Bangalore" , "Kolar" , "Dommalur" , Name="Dayananda", Age="29")

