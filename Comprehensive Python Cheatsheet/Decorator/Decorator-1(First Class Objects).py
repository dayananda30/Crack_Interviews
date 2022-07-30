'''

First Class Objects:
=====================
* In Python, functions are first class objects.
* This means that functions can be passed around and used as arguemnts just like String , int , float , list and so on.

'''

#Regular function which expects name given as a string
def say_hello(name):
    return "Hello {}".format(name)


#Regular function which expects name given as a string
def be_awesome(name):
    return "Daya and  {}, together we are the awesomest!".format(name)

#It expects a function as its arguement
def greet_bob(greeter_func):
    return greeter_func("Bob")


if __name__ == '__main__':
    print say_hello("Dayananda")
    print be_awesome("Nanda")
    print greet_bob(say_hello)
    print greet_bob(be_awesome)
