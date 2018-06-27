"""

one function can return another function
"""


def outer():
    print("I am outside of the inner function")
    def inner():
        print("I am inside inner function")
    return inner()


res = outer()
