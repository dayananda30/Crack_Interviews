from collections import Counter

list = ["daya", "nanda","daya", "nanda","daya", "nanda","daya", "nanda","daya", "nanda","daya", "nanda","daya", "nanda","daya", "nanda","daya", "nanda","daya"]

print(Counter(list))

print(Counter(list).most_common()[0])