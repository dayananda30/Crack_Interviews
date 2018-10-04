"""
Element.findall() finds only elements with a tag which are direct chiidren of the
current Element.find() finds the first child with a particular tag and Element.text
accesses the elements's text content.

Element.get() accesses the element's attributes.

"""

import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')

root = tree.getroot()

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print("The Country {} has secured {} rank".format(name,rank))
