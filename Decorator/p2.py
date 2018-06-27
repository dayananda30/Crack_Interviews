"""
functions taking another function as an arguement.
"""

def increment(x):
    return x +1

def decrement(x):
    return x-1

def operate(func,x):
    res = func(x)
    return res

out = operate(increment,3)

print(out)

out = operate(decrement,3)

print(out)


