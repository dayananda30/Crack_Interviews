def star(func):
    def inner(*args,**kwargs):
        print('*'*30)
        func(*args,**kwargs)
        print('*'*30)
    return inner

def percentage(func):
    def inner(*args,**kwargs):
        print('%'*30)
        func(*args,**kwargs)
        print('%'*30)
    return inner

@star
@percentage
def printer(msg):
    print(msg)




if __name__=="__main__":
    printer("HEY Decorators!!!")



"""
@star
@percent
def printer(msg):
    print(msg)
    
    
is equivalent to


def printer(msg):
    print(msg)
printer = star(percent(printer))




"""


