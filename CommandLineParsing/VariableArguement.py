def display(**kwargs):
    if kwargs.keys() is not None:
        for key in kwargs.keys():
            print("{} ==> {} ".format(key,kwargs[key]))



dict = {1:"one",2:"Two",3:"Three",4:"Four"}
print(dict)
display(number = "one", number2= "Two")
