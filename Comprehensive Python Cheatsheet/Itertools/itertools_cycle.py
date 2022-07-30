from itertools import *

print("The cycle() function returns an iterator that repeats the contents of the arguments it is given indefinitely. Since it has to remember the entire contents of the input iterator, it may consume quite a bit of memory if the iterator is long. In this example, a counter variable is used to break out of the loop after a few cycles.")

i = 0
for item in cycle(['a', 'b', 'c']):
    i += 1
    if i == 10:
        break
    print (i, item)
