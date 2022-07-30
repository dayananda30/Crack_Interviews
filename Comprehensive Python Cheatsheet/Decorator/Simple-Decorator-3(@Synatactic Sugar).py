def my_Decorator(func):
    def wrapper():
        print("*"*30)
        print("Before calling the function")
        print("@"*30)
        func()
        print("@"*30)
        print("After calling the function")
        print("*"*30)
    return wrapper

@my_Decorator
def say_whee():
    print("     Decorated Function    ")


if __name__ == '__main__':
    say_whee()
