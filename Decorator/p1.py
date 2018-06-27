"""
We all know that everything in python is object right from class and methods.

"""


def first(message):
    print(message)



first("Learning Decorator!!!")
second = first

second("Learning Decorator...")


"""
Here the name first and second refers to the same function object.
"""
