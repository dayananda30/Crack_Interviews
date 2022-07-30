import itertools

print("izip() returns an iterator that combines the elements of several iterators into tuples. It works like the built-in function zip(), except that it returns an iterator instead of a list.")
for i in itertools.izip([1, 2, 3], ["One", "Two", "Three"]):
    print i


print("when iterables length is not same :")
for i in itertools.izip([1, 2, 3], ["One", "Two", "Three"], ["X"]):
    print("*"*10)
    print i
