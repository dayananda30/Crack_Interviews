x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
'''
In Python 3.x 
==============
z = {**x, **y}
'''

z = dict(x,**y)
print("Merged Dict is : {}".format(z))

zz = dict(y,**x)
print("Merged Dict is : {}".format(zz))

'''
Source : https://stackoverflow.com/questions/21809112/what-does-tuple-and-dict-means-in-python

In python * represents positional arguement and ** means treat this as key-value pair.

Example:
def foo(x, y):
    print(x, y)

>>> t = (1, 2)
>>> foo(*t)
1 2

'''


