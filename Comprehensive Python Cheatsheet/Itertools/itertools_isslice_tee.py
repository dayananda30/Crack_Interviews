from itertools import *


print("The tee() function returns several independent iterators (defaults to 2) based on a single original input. It has semantics similar to the Unix tee utility, which repeats the values it reads from its input and writes them to a named file and standard output.")



r = islice(count(), 5)
i1, i2 = tee(r)

for i in i1:
    print 'i1:', i

print("*****")
for i in i2:
    print 'i2:', i
