"""
Nested functions can access outer function variables but not outside of the outside function.
It restricts the access sort of data hiding.

"""



def outer(message):
    text = message
    def inner():
        print("I am inside inner() function and {} is the message you have passed in the function call".format(text))
    inner()

#outer("Learning Closures in Python")


#print("#"*30)

#print("Closure returns the function object instead of calling the function")

def outer_closure(message):
    text = message
    def inner_closure():
        print("HEY!!!!!!!!!I am here and {} is your message".format(text))
    return inner_closure


if __name__ == "__main__":
    outer("Learning Closures")
    print("#"*30)
    res = outer_closure("How closure works")
    res()
