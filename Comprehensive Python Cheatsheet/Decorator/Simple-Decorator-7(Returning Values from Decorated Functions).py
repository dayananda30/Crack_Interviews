def my_decorator(func):
    def wrapper(*args):
        print("In Wrapper Function")
        #func(*args)
        return func(*args)
    return wrapper

@my_decorator
def add(*args):
    if args:
        print("Printing the sum in Normal Function : {}".format(sum(args)))
        return sum(args)

if __name__ == '__main__':
    add = add(5,5)
    print("Printing the Return Value from the Decorated Function : {}".format(add))


'''
Note : 
======
If you don't return from the decorated function , then you can't use that value in the main function. It will be None.

If you want to try this scenario , 
comment  return func(*args) line and uncomment func(*args) to see the difference.
'''
