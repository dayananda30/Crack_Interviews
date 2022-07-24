list_1 = [1, 2, 3]
list_2 = [5, 5, 6, 7]

unsorted_list = [5, 4, 3, 2, 1]

##################################################################################

"""
<list>.append(<el>) # Or: <list> += [<el>]
"""

print("Appending List with item 4")
list_1.append(4)
print(list_1)

##################################################################################

"""
<list>.extend(<collection>) # Or: <list> += <collection>
"""
print(list_1.extend(list_2))

##################################################################################

"""
<list> = sorted(<collection>)
"""
print(sorted(unsorted_list))

##################################################################################

"""
sum_of_elements = sum(<collection>)
"""

sum_of_elements = sum([1, 2, 3])
print(sum_of_elements)

##################################################################################

"""
elementwise_sum = [sum(pair) for pair in zip(list_a, list_b)]
"""
elementwise_sum = [sum(pair) for pair in zip([1, 2, 3], [1, 2, 3])]
print(elementwise_sum)

##################################################################################

"""
ZIP Examples :
Output:

0 Mukesh 24
1 Roni 50
2 Chari 18
"""
names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

##################################################################################

"""
ZIP example
{'reliance': 2175, 'infosys': 1127, 'tcs': 2750}
"""

stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(new_dict)

##################################################################################

"""
<int> = <list>.count(<el>) # Returns number of occurrences. 
"""

print([1, 2, 3, 1].count(1))

##################################################################################

"""
index = <list>.index(<el>) # Returns index of first occurrence or raises ValueError.
"""

print([1, 2, 3, 4, 5].index(5))

##################################################################################

"""
<list>.insert(index, <el>) # Inserts item at index and moves the rest to the right.
"""

list_3 = [1,2,3,4,5]
list_3.insert(0, "Beginning")
print(list_3)

##################################################################################

"""
<el> = <list>.pop([index]) # Removes and returns item at index or from the end.
"""

list_3.pop(0)
print(list_3)

##################################################################################

"""
<list>.remove(<el>) # Removes first occurrence of item or raises ValueError.
"""

list_3.remove(1)
print(list_3)

##################################################################################

"""
<list>.clear() # Removes all items. Also works on dictionary and set.
"""

list_3.clear()
print(list_3)

##################################################################################

