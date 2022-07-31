"""
Basic Example
try:
    <code>
except <exception>
    <code>


Complex Example
try:
    <code_1> // some lines of code which you may want to catch the exception
except <exception-a>
    <code_a>
except <exception-b>
    <code_b>
else:
    <remaining code>
finally:
    <code_finally>

code inside the 'else' block  will only be executed if 'try' block had no exceptions.
code inside 'finally' block will always be executed.

Catching Exceptions:
except <exception>:
except <exception> as <name>:
except (<exception>, ...):
except (<exception>, ...) as <name>:

Raising Exceptions:
raise <exception>
raise <exception>()
raise <exception>(<el> [, ...])

Re-Raising caught Exceptions
except <exception> as <name>:
    ...
    raise

BaseException
 ├── SystemExit # Raised by the sys.exit() function.
 ├── KeyboardInterrupt # Raised when the user hits the interrupt key (ctrl-c).
 └── Exception # User-defined exceptions should be derived from this class.
 ├── ArithmeticError # Base class for arithmetic errors.
 │ └── ZeroDivisionError # Raised when dividing by zero.
 ├── AttributeError # Raised when an attribute is missing.
 ├── EOFError # Raised by input() when it hits end-of-file condition.
 ├── LookupError # Raised when a look-up on a collection fails.
 │ ├── IndexError # Raised when a sequence index is out of range.
 │ └── KeyError # Raised when a dictionary key or set element is not found.
 ├── NameError # Raised when a variable name is not found.
 ├── OSError # Failures such as “file not found” or “disk full”.
 │ └── FileNotFoundError # When a file or directory is requested but doesn't exist.
 ├── RuntimeError # Raised by errors that don't fall in other categories.
 │ └── RecursionError # Raised when the maximum recursion depth is exceeded.
 ├── StopIteration # Raised by next() when run on an empty iterator.
 ├── TypeError # Raised when an argument is of wrong type.
 └── ValueError # When an argument is of right type but inappropriate value.
 └── UnicodeError # Raised when encoding/decoding strings to/from bytes fails.

"""