"""
Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
The iterator object is initialized using the iter() method. It uses the next() method for iteration.

__iter(iterable)__ method that is called for the initialization of an iterator. This returns an iterator object
next ( __next__ in Python 3) The next method returns the next value for the iterable.

"""

# Here is an example of a python inbuilt iterator
# value can be anything which can be iterated
iterable_value = 'Dayananda'
iterable_obj = iter(iterable_value)

while True:
    try:
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        # exception will happen when iteration will over
        break


# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:
    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 0
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1;
        return x


print("Print numbers from 0 to 15")
for i in Test(15):
    print(i)

print("Print numbers from 0 to 5")
for i in Test(5):
    print(i)
