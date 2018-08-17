from itertools import *

print("The repeat() function returns an iterator that produces the same value each time it is accessed. It keeps going forever, unless the optional times argument is provided to limit it.")


for i in repeat('over-and-over', 5):
    print i



print("It is useful to combine repeat() with izip() or imap() when invariant values need to be included with the values from the other iterators.")

for i, s in izip(count(), repeat('over-and-over', 5)):
    print i, s
