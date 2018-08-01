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


if __name__ == "__main__":
    dog = Dog()
    dog.eating()
    dog.barking()
