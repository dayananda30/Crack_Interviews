
'''
XAPTH Supported
'''

import xml.etree.ElementTree as ET

root = ET.fromstring('country')

# Top-level elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")




"""

Supported XPath syntax:
========================
.       Selects the current node.This is mostly useful 
        at the beginning of the path to indicate that it's a relative path
        
//      Selects all the subelements on all the levels beneath the current element.
        Eg. .//table -> selects all table elements in the entire tree.
        
..      Selects the parent element.

[@attrib]       Selects all elemnts that have the given attribute.

[@atrib='value']        Selects all elements for which the given attribute has the given value.

[tag]       Selects all elements for which that have a child named tag. Only immediate children supported.

[tag='text']


"""
