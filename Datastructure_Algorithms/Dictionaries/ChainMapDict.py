'''
The Collections.ChainMap data structure groups multiple dictionaries into a single mapping.

Insertion and Deletions and lookup only affects the first mapping added to the chain.
i.e performs will not effect to the existing dict.

'''


from collections import ChainMap
dict1 = {'one':1,'two':2}
dict2 = {'three':3,'four':4}
chain = ChainMap(dict1,dict2)
print(chain)
chain['one']
