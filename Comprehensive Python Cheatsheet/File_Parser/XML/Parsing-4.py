"""
Modifying an XML file

ElementTree.write() provides a simple way to build XML documents and write them to files.

Once created, an Element object may be manipulated by directly changing its fileds(such as Element.text),
adding and modifying attributes(Element.set() method) as well as adding new children (eg: Element.append())



Here in this example
we want to add one point extra to country's rank and add an updated attribute to the rank element.



Before :
=======
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>



After:
======
    <country name="Liechtenstein">
        <rank updated='yes'>2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>


To Remove any Element in an XML Doc:
=====================================
for country in root.findall('country'):
	rank = int(country.find('rank').text)
	if rank > 50:
		root.remove(country)
tree.write('output.xml')
"""

import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')

root = tree.getroot()

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = new_rank
    rank.set('updated','yes')
tree.write('output.xml')
