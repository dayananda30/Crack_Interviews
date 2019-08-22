#  Find the ten most common words in Hamlet


import re
from collections import Counter

#words = re.findall(r'\w+',open('example.txt').read().lower())
words = []
pattern = re.compile(r'(\w+)')
with open('example.txt') as f:
    for line in f.readlines():
        word = pattern.findall(line)
        for item in word:
            words.append(item)

print words

cnt = Counter(words)

print(type(words)) # Regex applies on the file and put all the strings into a list

print Counter(words).most_common(10)
