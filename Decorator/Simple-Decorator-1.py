def my_decorator(func):
    def wrapper():
        print("Before function got executed")
        func()
        print("After function got executed")
    return wrapper

def say_whee():
    print("Whee!")



say_whee = my_decorator(say_whee)
say_whee()
