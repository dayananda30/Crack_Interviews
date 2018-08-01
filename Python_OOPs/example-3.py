class parent1:
    def __init__(self):
        print("Parent1 Constructor !!!")

    def display_paretn1(self):
        print("Displaying Parent 1")

class parent2:
    def __init__(self):
        print("Parent2 Constructor !!!")

    def display_paretn2(self):
        print("Displaying Parent 2")

class DerivedClass(parent1,parent2):
    def __init__(self):
        print("Derived Class Constructor")

    def display(self):
        print("Diplaying Derived Class")


if __name__ == '__main__':

    obj = DerivedClass()
    obj.display_paretn1()
    obj.display_paretn2()
    obj.display()


