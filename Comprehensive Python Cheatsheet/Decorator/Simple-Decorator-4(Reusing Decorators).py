'''
* Decorator is just a regualr Python function.
* Let's move the decorator to its own module that can be used in many other functions.

Library:

'''

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
