#  Find the ten most common words in Hamlet


import re
from collections import Counter

words = re.findall(r'\w+',open('example.txt').read().lower())

print words

print(type(words)) # Regex applies on the file and put all the strings into a list

print Counter(words).most_common(10)
