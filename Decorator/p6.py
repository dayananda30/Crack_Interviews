
def smartdivide(func):
    def inner(a,b):
        if b == 0:
            print("Whoops !!! Division not possible")
            return
        else:
            return func(a,b)
    return inner

@smartdivide
def divide(a,b):
    return a/b


"""
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner
"""

if __name__ == "__main__":
    res = divide(2,0)
    print(res)
    res = divide(2,2)
    print(res)
