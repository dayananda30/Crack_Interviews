import json
from pprint import pprint

with open('Data.json') as f:
    data = json.load(f)

pprint(data)

print "******************* You can retrieve any value like below: ***********************"

print(data["maps"][0]["id"])
print(data["masks"]["id"])
print(data["om_points"])
#print()
