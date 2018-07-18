'''
MappingProxtType is a wrapper for making Read only Dictionaries

This class is added in python 3.3 and it can be used create immutable proxy versions of dictionaries.

'''


from types import MappingProxyType

mutable = {'one':1, 'two':2}

immutable = MappingProxyType(mutable)


immutable['one']
# Output is 1

immutable['one'] = 11
#Type Error


''' 
Interesting:

Updates to Mutable will reflect in the immutable proxy.
'''

mutable['one'] = 123
immutable['one']
#output : 123
