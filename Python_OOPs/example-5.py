class Parent(object):
    def __init__(self):
        print("I am in Parent Contructor!")

class Child(Parent):
    def __init__(self,item):
        self.item = item
        super(Child,self).__init__()
        print("The data that you have passed is : {}".format(self.item))


if __name__ == '__main__':
    c = Child('Dayananda')
