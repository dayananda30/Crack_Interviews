def display(name,*args):
    print("{} is a fixed arg that anyway you need to pass it".format(name))
    for i in args:
        print("{} is a variable arg".format(i))


display("India")
print("*"*20)
display("India","Nepal","Srilanka","Pakistan")
