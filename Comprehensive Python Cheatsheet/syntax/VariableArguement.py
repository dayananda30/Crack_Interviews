def display(**kwarg):
    if kwarg.keys() is not None:
        for key in kwarg.keys():
            print("{} ==> {} ".format(key, kwarg[key]))


dict = {1: "one", 2: "Two", 3: "Three", 4: "Four"}
print(dict)
display(number="one", number2="Two")
