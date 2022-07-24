"""
<str> = <str>.strip() # Strips all whitespace characters from both ends.
"""
s = "     Dayananda    "
print(s)
print(s.strip())

##########################################################################################
"""
<list> = <str>.split() # Splits on one or more whitespace characters.
"""
s = "123Monday123"
print(s)
print(s.strip("123"))

##########################################################################################

"""
<list> = <str>.split(sep=None, maxsplit=-1) # Splits on 'sep' str at most 'maxsplit' times.
"""

s = "dayananda30@gmail.com"
print(s.split(sep="@"))

##########################################################################################

"""
<list> = <str>.splitlines(keepends=False) # Splits on \n,\r,\r\n. Keeps them if 'keepends'.
"""

s = "I had a dove \n and sweet dove is died \r I thought of its died of grieving \r "
print(s.splitlines())
print(s.splitlines(keepends=True))

##########################################################################################
"""
<str> = <str>.join(<coll_of_strings>) # Joins elements using string as separator.
"""
list1 = ['1', '2', '3', '4']
s = "-"
# joins elements of list1 by '-'
# and stores in string s
s = s.join(list1)
print(s)

##########################################################################################

list1 = ['D', 'a', 'y', 'a', 'n', 'a', 'n', 'd', 'a']
print("".join(list1))

##########################################################################################
"""
<bool> = <str>.startswith(<sub_str>) # Pass tuple of strings for multiple options.
<bool> = <str>.endswith(<sub_str>) # Pass tuple of strings for multiple options.
"""

s = "dayananda"
print(s.startswith("day"))
print(s.endswith("da"))

##########################################################################################
"""
<int> = <str>.find(<sub_str>) # Returns start index of first match or -1.
<int> = <str>.index(<sub_str>) # Same but raises ValueError if missing.
"""

s = "Findmeifyoucan"
print(s.find("me"))
print(s.index("me"))

##########################################################################################
"""
<str> = <str>.replace(old, new [, count]) # Replaces 'old' with 'new' at most 'count' times.
"""
print(s)
print(s.replace("Find", "DonotFind"))

