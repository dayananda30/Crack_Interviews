"""
class methods useful to instantiate objects (constructor).

Difference between static methods and class methods

class methods by default take class as first argument whereas static methods doesn't take class as first parameter.

"""

class Employee:
    pay_hike = 11.0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @staticmethod
    def display_payhike():
        return Employee.pay_hike

    @staticmethod
    def update_payhike(new_payhike):
        Employee.pay_hike = new_payhike

    @classmethod
    def from_string(cls, input_string):
        first_name, last_name, pay = input_string.split("-")
        return cls(first_name, last_name, pay)


if __name__:
    print(Employee.display_payhike())
    Employee.update_payhike(12.0)
    print(Employee.display_payhike())

    employee1 = "Daya-Nanda-50000"
    employee2 = "bob-job-60000"
    emp1 = Employee.from_string(employee1)
    emp2 = Employee.from_string(employee2)

    print(emp1.first_name)
    print(emp2.first_name)
