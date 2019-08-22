# Tally(Total) occurrences of words in a list

from collections import Counter

cnt = Counter()
print(type(cnt))

#print("Printing Empty Counter: {}".format(cnt))

list = ['one','two','one','three','four','three','four','one','two','one','three','four','three','four']


for word in list:
    cnt[word] = cnt[word] + 1


print(cnt)


# To put it in a  proper format

c = Counter(list)
print(c)

for word in set(list):
    print('{} : {}'.format(word,c[word]))
