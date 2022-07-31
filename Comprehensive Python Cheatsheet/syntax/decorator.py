def debug(func):
    def wrapper(*args, **kwargs):
        print("Decorating the Function".format())
        return func(*args, **kwargs)

    return wrapper


@debug
def add_numbers(x, y):
    return x + y


if __name__ == "__main__":
    print(add_numbers(1, 2))
