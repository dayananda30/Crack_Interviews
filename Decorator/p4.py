def makepretty(func):
    def inner():
        print("I am decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

print("*********  This is ordinary **************")
ordinary()

print("*******************************************")

print("********  How Decorators Works!  **********")

pretty = makepretty(ordinary)
pretty()

print("*******************************************")



"""
Any functions or methods are callable as they can be called.

In Python, any object which is implemented __call__() method is termed callabale.

Usually Decorators takes in a function object and adds some functionality and returns it.



In the above example , makepretty is the decorator.

ord = makepretty(ordinary) // Decorator is adding more functionality to the ordinary function object.

The function ordinary is got decorated.

This is similar to packaging a gift. Decorator acts as a wrapper.




"""
