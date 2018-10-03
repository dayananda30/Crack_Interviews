import json
dict = {1:'one', 2:'two'}
jobj = json.dumps(dict, separators=(',',': '), sort_keys=True, indent=4)
print jobj
