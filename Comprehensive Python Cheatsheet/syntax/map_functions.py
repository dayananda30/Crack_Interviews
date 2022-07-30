"""
The map() function is a higher-order function.
As previously stated,this function accepts another function and a
sequence of ‘iterables’ as parameters and provides output after applying the function
to each iterable in the sequence. It has the following syntax:

SYNTAX: map(function, iterables)

Here the function might be user defined function using def or lamda function.

Daya Hint:
When writing a function, assume your function is taking one item in the list instead of whole list.
"""


def add_five(number):
    return number + 5


print(list(map(add_five, [1, 2, 3])))

print(list(map(lambda x: x + 5, [1, 2, 3])))
