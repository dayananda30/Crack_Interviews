'''
Inner Functions:
================
* Inner functions are defined inside parent function.
* The order in which the inner functions are defined doesn't matter.
* Inner functions are not defined until the parent function is called.
* Inner functions are locally scoped and exist inside the parent() as local variables.

'''


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

if __name__ == "__main__":
    parent()
