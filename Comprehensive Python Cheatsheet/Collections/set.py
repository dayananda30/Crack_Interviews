"""
<set> = set()
<set>.add(<el>) # Or: <set> |= {<el>}
"""

my_set = set([1, 2, 3])
print(my_set)
my_set.add(4)
my_set |= {5}
print(my_set)

##################################################################################
"""
<set> = <set>.union(<coll.>) # Or: <set> | <set>
"""

print(my_set.union([6, 7]))

##################################################################################
"""
"<set> = <set>.intersection(<coll.>) # Or: <set> & <set>
"""

print(my_set.intersection([1, 2, 3]))

##################################################################################

"""
<set> = <set>.difference(<coll.>) # Or: <set> - <set>
"""

##################################################################################
"""
<bool> = <set>.issubset(<coll.>) # Or: <set> <= <set>
"""

print(my_set.issubset([1,2]))

##################################################################################
"""
<bool> = <set>.issuperset(<coll.>) # Or: <set> >= <set>
"""

print(my_set.issuperset([2]))

##################################################################################
"""
<el> = <set>.pop() # Raises KeyError if empty.
"""
res = my_set.pop()
print(res)
print(my_set)

##################################################################################
"""
<set>.remove(<el>) # Raises KeyError if missing.
"""

my_set.remove(2)
print(my_set)

##################################################################################
"""
<set>.discard(<el>) # Doesn't raise an error.
"""

my_set.discard(89)
