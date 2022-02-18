"""
Method resolution order:
    Developer
    Employee
    builtins.object
"""


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + "." + self.last + "@email.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay + self.raise_amt


class Developer(Employee):
    pass


dev1 = Developer("Daya", "Nanda", 80000)
dev2 = Developer("Bob", "Harley", 10000)

print(help(Developer))

# print(dev1.fullname())
# print(dev2.fullname())
