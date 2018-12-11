# Python code to demonstrate namedtuple() and
# Access by name, index and getattr()

# importing "collections" for namedtuple()


from collections import namedtuple


#Declaring a NamedTuple
Student = namedtuple('Student',['Name','Age','DOB'])


#Adding Values
S = Student('Dayananda','29','31-07-1990')


print("Displaying the NamedTuple: {}".format(S))

#Access Using Index
print("Name of the Student using index  : {}".format(S[0]))


#Access Using key
print("Age of the Student Using key  :  {}".format(S.Age))


#Access Using getAttr()
print("DOB of the Student using getAttr() is : {} ".format(getattr(S,'DOB')))
