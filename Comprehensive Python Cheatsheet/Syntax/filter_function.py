"""
The filter() function is used to generate an output list of values that return true
when the function is called. It has the following syntax:

SYNTAX: filter (function, iterables)

"""


def get_above_10(number):
    if number > 10:
        return 10

print(list(filter(get_above_10, [1, 2, 3, 11, 89, 100])))
