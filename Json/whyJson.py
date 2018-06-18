import json

#without using json

print "Data format without Using JSON"

list = []
list.append({"Name":"Dayananda","Age":"28"})
list.append({"Name":"Smith","Age":"85"})
list.append({"Name":"Gilchrist","Age":"68"})
print list

print "After Using JSON for formatting data"
print json.dumps(list,indent=4,separators=(",",":"),sort_keys=True)
