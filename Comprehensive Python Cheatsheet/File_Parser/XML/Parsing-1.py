'''
Loading xml file.
Finding the root of the tree.
Iterating over second level of the tree.
Printing node tag name, attributes and values.

'''

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')

root = tree.getroot()


print('"{}" is the root of the element tree in this xml Doc'.format(root.tag))


for child in root:
    print("*"*25)
    print('{} : {}'.format(child.tag,child.attrib))
    print("*"*25)
    for innerchild in child:
        print('{} : {} : {}'.format(innerchild.tag,innerchild.attrib,innerchild.text))

print("@"*50)
print("Another way of getting values:")
print(root[0][1].text)
