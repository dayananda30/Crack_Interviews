"""
What if we want to add new input developer class in the constructor?
example: programming_language
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
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language


dev1 = Developer("Daya", "Nanda", 80000, "Python")
dev2 = Developer("Bob", "Harley", 10000, "Java")

print(dev1.prog_language)
print(dev2.prog_language)
