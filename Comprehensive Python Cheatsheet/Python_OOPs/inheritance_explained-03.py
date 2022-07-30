"""
__repr__() and __str__() special methods
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

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language


dev1 = Developer("Daya", "Nanda", 80000, "Python")
dev2 = Developer("Bob", "Harley", 10000, "Java")

print(dev1)
print(dev1.__repr__())
print(dev2.__str__())
