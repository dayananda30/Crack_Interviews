from collections import Counter


c  = Counter('abcdabcdabababababababbababadddddddddddddddddd')

print('Printing the elments and their occurances : {}'.format(c))


print("Printing only the elements : {}".format(list(c.elements())))


print("Printing the two most common element based on the occurences : ".format(c.most_common(2)))






