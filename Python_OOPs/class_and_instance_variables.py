"""
Instance variables are tied to particular instances and can vary across instances
Class variables are same across all the instances of that class.

By default, class variables doesn't list under instance namespace
Once instance overrides class variables, class variables does appear under instance namespace.

"""


class Employee:
    # Class Variables
    pay_raise = 11
    num_of_employees = 0

    def __init__(self, first_name, last_name, net_pay):
        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.net_pay = net_pay
        Employee.num_of_employees = Employee.num_of_employees + 1

    def apply_pay_raise(self):
        self.net_pay = int(self.net_pay) + self.pay_raise

    def get_employee_details(self):
        print("Employee Name: {} {}".format(self.first_name, self.last_name))
        print("Net Pay : {}".format(self.net_pay))

    @staticmethod
    def get_total_employees():
        print("The Total Number of employees : {}".format(Employee.num_of_employees))


if __name__ == '__main__':
    e1 = Employee("Daya", "Nanda", "50000")
    e2 = Employee("Deepu", "Geetha", "60000")

    e1.get_employee_details()
    e2.get_employee_details()
    print("*" * 30)

    print("Even though pay_raise and num_of_employees variables are part of class and they won't be part of instance "
          "object Namespace until and unless it is overriden by an instance ")
    print(e1.__dict__)
    print("*" * 30)

    e1.apply_pay_raise()

    e2.pay_raise = 19  # Overriding class variable on instance level
    e2.apply_pay_raise()

    print("Employee salary change after hike")
    e1.get_employee_details()
    e2.get_employee_details()
    print("*" * 30)

    print("Now instance Namespace has pay_raise attribute")
    print(e2.__dict__)

    print("*" * 30)
    print("The total number of employees: {}".format(Employee.num_of_employees))
