class Animal:
    def __init__(self):
        print("I am in Parent class Constructor!!!")

    def eating(self):
        print("Eating in the Parent Class")


class Dog(Animal):
    def __init__(self):
        print("I am in Child class Contructor!!!")

    def barking(self):
        print("Dog is Barking  in the Child class")


class BabyDog(Dog):
    def __init__(self):
        print("I am in BabyConstructor class")

    def weep(self):
        print("Weeping............")
if __name__ == "__main__":
    dog = BabyDog()
    dog.eating()
    dog.barking()
    dog.weep()
