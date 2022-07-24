from collections import namedtuple

# Declaring Nametuple
Student = namedtuple('Student', ['Name','Age','DOB'])

# Adding Values
s = Student('Dayananda', 32, 1990)

# Access using index
print("The Student Age using index is : {} ".format(s[1]))

# Access using name
print("The Student name using keyname is : {}".format(s.Name))

# Access using getattr()
print("The Student DOB using getattr() is : {}".format(getattr(s, 'DOB')))

# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(s._fields)

