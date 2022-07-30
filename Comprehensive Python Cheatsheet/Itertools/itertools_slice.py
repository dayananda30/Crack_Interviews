#import itertools


print("The islice() function returns an iterator which returns selected items from the input iterator, by index. It "
      "takes the same arguments as the slice operator for lists: start, stop, and step. The start and step arguments "
      "are optional.")


from itertools import *


print('Stop at 5:')
for i in islice(count(), 5):
    print(i)

print('Start at 5, Stop at 10:')
for i in islice(count(), 5, 10):
    print(i)

print('By tens to 100:')
for i in islice(count(), 0, 100, 10):
    print(i)

