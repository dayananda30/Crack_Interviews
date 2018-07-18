'''
Python includes a specilised dict subclass that remembers the insertion order of keys added to it.

While standard dict instances preserved the insertion order of the keys in CPython 3.6 and above.


When it is useful:
When your algorithm/code logic needs key order then you must explictly should use this OrderDict class.


Note:
    orderedDict is not built in and must inport in the standard library.
'''

from collections import OrderedDict

d = OrderedDict([('one',1),('two',2),('three',3)])
print("The Dictionary Content is : {}".format(d))
print("The Dictionary Keys are : ".format(d.keys()))
print("The Dictionary values are {}".format(d.values()))
if d.has_key("one"):
    print("The Key 'one' is present in the dict")
else:
    print("The key 'one' is not present in the Dict")
if d.has_key('five'):
    print("The Key 'Five' is  present in the Dict")
else:
    print("The Key 'Five' is not present in the Dict")
print("The Size of the Dict is {}".format(d.__sizeof__()))
print("The length of the Dict is {}".format(len(d.values())))



