def my_decorator_print_asteric(func):
    def wrapper():
        print("*"*100)
        func()
        print("*"*100)
    return wrapper


def my_decorator_print_percentage(func):
    def wrapper():
        print("%"*100)
        func()
        print("%"*100)
    return wrapper

@my_decorator_print_asteric
@my_decorator_print_percentage
def my_func():
    print("Nested Decorators are evaluated in the same order as they passed : decorater1(decorater2(function)) ")

if __name__ == '__main__':
    my_func()




