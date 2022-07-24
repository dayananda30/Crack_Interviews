"""
The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state
to enable function to resume where it is left off. When resumed, the function continues execution immediately after
the last yield run. This allows its code to produce a series of values over time, rather than computing them at once
and sending them back like a list.

"""


# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1  # 1st iteration in for loop and rest of the code pause its execution.
    yield 2  # This yield resumes in second iteration and rest of the code paused.
    yield 3  # This yield resumes in third iteration.


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


#####################################################################################################

# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)
