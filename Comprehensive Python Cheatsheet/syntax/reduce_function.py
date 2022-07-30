from functools import reduce

"""
The reduce() function applies a provided function to ‘iterables’ and returns a single value,
as the name implies.
"""


def get_sum_of_all(a, b):
    return a + b


print(reduce(get_sum_of_all, [1, 2, 3, 4, 5]))
