dict = {'a':4,'b':5,'c':1,'d':3,'e':2}


print("Sorting Based on keys")
print(sorted(dict.items(),key=lambda x: x[0]))

print("Sorting Based on values")
print(sorted(dict.items(),key=lambda x: x[1]))









