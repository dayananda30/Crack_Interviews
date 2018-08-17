from itertools import *
print("The count() function returns an interator that produces consecutive integers, indefinitely. The first number can be passed as an argument, the default is zero. There is no upper bound argument (see the built-in xrange() for more control over the result set). In this example, the iteration stops because the list argument is consumed.")


from itertools import *

for i in izip(count(1), ['a', 'b', 'c', 'd', 'e']):
    print i
