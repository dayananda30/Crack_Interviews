'''
DefaultDict is another subclass the aceepts callable in its constructor i.e list

Advantages:
This can save some typing time.


In this example list is a empty list.
Accessing a missing key creates it and initialises it using the default factory.
'''

from collections import defaultdict

dd = defaultdict(list)
dd['nations'].append('India')
dd['nations'].append('Srilanka')
dd['nations'].append('Nepal')
dd['nations'].append('Pakistan')

print("Key is {}".format(dd.keys()))
print("Nations are {}".format(dd.values()))

print(dd['nations'])



