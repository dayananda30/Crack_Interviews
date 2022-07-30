""""
for loops also have an else clause.
The else clause executes after the loop completes normally.
This means that the loop did not encounter a break statement.
One Common Usage is to check whether loop ends or not.
we can check it via flag but for else is preferred way
"""

fruits = ['Apple', 'banana', 'orange']
for fruit in fruits:
    if fruit == 'Mango':
        print("It is a Mangoo Season and It is the king of the fruit")
        break
else:
    print("This is not a Mango Season !!!! of Course it is the king of the fruit")
