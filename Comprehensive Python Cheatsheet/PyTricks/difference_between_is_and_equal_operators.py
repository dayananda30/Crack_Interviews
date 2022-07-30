'''
Same and identical are different

== --> returns True if two object content is equal
is  --> returns True if two objects are identical

'''

listB = [1,2,3]
listA = listB
print("Evaluating 'is' Operator : ")
if listA is listB:
    print('"{}" and "{}" are identical'.format(listA,listB))
    print("ID of ListA is {} and ID of ListB is {}".format(id(listA),id(listB)))

else:
    print('"{}" and "{}" are not identical'.format(listA,listB))
    print("ID of ListA is {} and ID of ListB is {}".format(id(listA),id(listB)))


print('*'*30)
print("Evaluating '==' Operator : ")

if listA == listB:
    print('"{}" and "{}" are equal'.format(listA,listB))
    print("ID of ListA is {} and ID of ListB is {}".format(id(listA),id(listB)))

else:
    print('"{}" and "{}" are not equal'.format(listA,listB))
    print("ID of ListA is {} and ID of ListB is {}".format(id(listA),id(listB)))


listC = [1,2,3]
print("Evaluating 'is' Operator : ")
if listA is listC:
    print('"{}" and "{}" are identical'.format(listA,listC))
    print("ID of ListA is {} and ID of ListB is {}".format(id(listA),id(listC)))

else:
    print('"{}" and "{}" are not identical'.format(listA,listC))
    print("ID of ListA is {} and ID of ListB is {}".format(id(listA),id(listC)))


print('*'*30)
print("Evaluating '==' Operator : ")

if listA == listC:
    print('"{}" and "{}" are equal'.format(listA,listC))
    print("ID of ListA is {} and ID of ListB is {}".format(id(listA),id(listC)))

else:
    print('"{}" and "{}" are not equal'.format(listA,listC))
    print("ID of ListA is {} and ID of ListB is {}".format(id(listA),id(listC)))

