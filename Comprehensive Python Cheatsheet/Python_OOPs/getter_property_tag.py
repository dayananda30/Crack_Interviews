""""
In below class,

Changing the first name, doesn't reflect the same change in email address.

we can bypass this error by adding a new function for email and calling that function but that again breaks
code base for already consuming existing email address.

Property tags are used to access methods as attributes
"""


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first + "." + self.last + "@email.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp1 = Employee("Daya", "nanda")
emp1.first = "Soma"

print(emp1.first)
print(emp1.email)


# SOLUTION
class Employees:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # Create a function with the same as email attribute
    @property
    def email(self):
        return self.first + "." + self.last + "@email.com"


emp2 = Employees("Daya", "nanda")
emp2.first = "Soma"

print(emp2.first)
print(emp2.email)
