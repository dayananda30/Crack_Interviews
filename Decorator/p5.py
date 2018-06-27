def makepretty(func):
    def inner():
        print("I am got Decorated!!!!")
        func()
    return inner


def anotherdecorator(func):
    def inner():
        print("I am also another decorated!!!")
        func()
    return inner

@makepretty
def ordinary():
    print("I am ordinary")

@anotherdecorator
def ord():
    print("I am Dayananda")


if __name__ == "__main__":
    print("####################################")
    ordinary()
    print("####################################")
    ord()
    print("####################################")





"""
@make_pretty
def ordinary():
    print("I am ordinary")
    
    
is equaivalent to 


def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

"""
