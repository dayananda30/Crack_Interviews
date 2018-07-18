'''
Tuple : Immutable containers


'''


t1 = (1,2,3)  # or t1 = 1,2,3
print("The id of t1 : {}".format(id(t1)))
t1 = (1,2,3)
print("The id of t1 : {}".format(id(t1)))


l1 = [1,2]
print("The id of l1 : {}".format(id(l1)))

l1.append(3)
print("The id of l1 : {}".format(id(l1)))

print("#######################")

print("Tuples can hold arbitary data types")
print("Addinf Data types creates a copy of the tuple.")
arr = "one","two","three"
print(arr)
print(arr+(23,))
