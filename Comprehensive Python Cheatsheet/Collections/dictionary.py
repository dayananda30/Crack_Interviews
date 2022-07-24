my_dict = {1: "one", 2: "two"}

##################################################################################
"""
<view> = <dict>.keys() # Coll. of keys that reflects changes.
"""

print(my_dict.keys())

##################################################################################
"""
<view> = <dict>.values() # Coll. of values that reflects changes.
"""

print(my_dict.values())

##################################################################################
"""
<view> = <dict>.items() # Coll. of key-value tuples that reflects chgs.
"""

print(my_dict.items())

##################################################################################
"""
value = <dict>.get(key, default=None) # Returns default if key is missing.
"""

print(my_dict.get(1))

##################################################################################
"""
Insert key with a value of default if key is not in the dictionary.        
Return the value for key if key is in the dictionary, else default.
"""
print(my_dict.items())
print(my_dict.setdefault(3, "three"))
print(my_dict.items())

##################################################################################
"""
<dict> = collections.defaultdict(<type>) # Creates a dict with default value of type.
https://www.geeksforgeeks.org/defaultdict-in-python/

defaultdict is similar to setdefault but setdeafult is operate on each item where as 
defaultdict operates on entire dict hence defaultdict is faster than setdefault.

setting default value at dictionary level when key is not present in the dictionary
instead of throwing KeyError

example: 

Traceback (most recent call last):
  File "dictionary.py", line 11, in 
    print(Dict[4])
KeyError: 4
"""

from collections import defaultdict


def default_value():
    return "Key Not Present"


my_dict1 = defaultdict(default_value)
my_dict1["a"] = 1
my_dict1["b"] = 2

print(my_dict1["a"])
print(my_dict1["b"])
print(my_dict1["c"])

"""
Output:
1
2
Key Not Present
"""

##################################################################################
"""
<dict> = dict(<collection>) # Creates a dict from coll. of key-value pairs.
"""

my_dict2 = dict([(1, "one"), (2, "two")])
print(my_dict2)

##################################################################################
"""
<dict>.update(<dict>) # Adds items. Replaces ones with matching keys.
"""

old_dict = {1: "one", 2: "two"}
old_dict.update({1: "ondu", 3: "three"})
print(old_dict)

##################################################################################
"""
value = <dict>.pop(key) # Removes item or raises KeyError.
"""

old_dict.pop(3)
print(old_dict)

##################################################################################
"""
{k for k, v in <dict>.items() if v == value} # Returns set of keys that point to the value.
"""

for key, value in my_dict.items():
    print("{} --> {}".format(key, value))

####################################################################################
""""
Sorting Dictionary Keys
"""

from collections import OrderedDict

unsorted_dict = {'ten': '10', 'nine': '9',
                 'fifteen': '15', 'two': '2', 'thirtytwo': '32'}
dict1 = OrderedDict(sorted(unsorted_dict.items()))
print(dict1)


