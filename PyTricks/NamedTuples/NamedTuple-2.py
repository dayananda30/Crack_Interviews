from collections import namedtuple


Student = namedtuple('Students',['Name','Age','DOB'])

s = Student('Daya','29','31071990')
print(s)

print('Printing all the fileds of Student NamedTuple : {}'.format(s._fields))


# using _replace() to change the attribute values of namedtuple
print ("The modified namedtuple is : ")
print(s._replace(Name = 'Dayananda D R'))
