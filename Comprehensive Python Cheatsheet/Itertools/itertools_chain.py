'''https://pymotw.com/2/itertools/ The chain() function takes several iterators as arguments and returns a single
iterator that produces the contents of all of them as though they came from a single sequence.

'''


import itertools

print("*"*10)
print("")
for i in itertools.chain("ABC", "DEF"):
    print(i)




#print(itertools.chain("Daya","Nanda"))








