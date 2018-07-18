'''
Lists are a part of the core python lanaguage.
Despite their name,Python's lists are implemented as dynamic arrays. behind the scenes.

It allows multiple data types is a powerfulr feature but it has downside as well.

multiple data types at the same time is generally less tighly packed as a result the whole structure takes much space.

'''


arr = ['one','two','three']

print arr

#del arr[1]

if arr.__contains__('one'):
    print("It is there")
else:
    print("it is not there")

print("The index of two is {}".format(arr.index('two')))
