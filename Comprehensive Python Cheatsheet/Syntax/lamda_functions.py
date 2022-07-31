"""
Python Lambda Functions are anonymous function means that the function is without a name.

Syntax:
lambda arguments: expression

This function can have any number of arguments but only one expression, which is evaluated and returned.

"""

lamdbda_print = lambda input_string: print(input_string)
lamdbda_print("Learning Lamda function")

lamdbsa_cube = lambda number: number * number * number
print(lamdbsa_cube(5))

# We can supply argument in lambda function itself
(lambda x: print(x + 1))(2)

tables = [lambda x=x: 10 * x for x in range(1, 11)]
print("The Length of the list : {}".format(len(tables)))
for table in tables:
    print(table())

# Lambda function with if else statement
(lambda x: print("{} is Positive Number".format(x)) if (x >= 0) else print("{} is Negative Number".format(x)))(-1)
(lambda x: print("{} is Positive Number".format(x)) if (x >= 0) else print("{} is Negative Number".format(x)))(1)

