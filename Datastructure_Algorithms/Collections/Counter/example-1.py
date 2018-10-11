# Tally(Total) occurrences of words in a list


from collections import Counter

cnt = Counter()

#print("Printing Empty Counter: {}".format(cnt))


for word in ['one','two','one','three','four','three','four','one','two','one','three','four','three','four']:
    cnt[word] = cnt[word] + 1


print(cnt)
