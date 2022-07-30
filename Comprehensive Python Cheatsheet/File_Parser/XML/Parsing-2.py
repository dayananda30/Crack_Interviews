"""
Finding interesting elements.
Eleemnt has some useful methods that help iterating recursively over all the sub tree below it
i.e(its children,their children and so on)

"""
import xml.etree.ElementTree as ET



tree = ET.parse('country_data.xml')
root = tree.getroot()

for neighbour in root.iter('neighbor'):
    print(neighbour.attrib)
