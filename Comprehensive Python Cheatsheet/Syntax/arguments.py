import argparse

"""
from argparse import ArgumentParser, FileType
p = ArgumentParser(description=<str>)
p.add_argument('-<short_name>', '--<name>', action='store_true') # Flag
p.add_argument('-<short_name>', '--<name>', type=<type>) # Option
p.add_argument('<name>', type=<type>, nargs=1) # First argument
p.add_argument('<name>', type=<type>, nargs='+') # Remaining arguments
p.add_argument('<name>', type=<type>, nargs='*') # Optional arguments
args = p.parse_args() # Exits on error.
value = args.<name>

"""

# Initializing Parser
parser = argparse.ArgumentParser(description='sort some integers.')

# Adding Argument
parser.add_argument('integers',
                    metavar='N',
                    type=float,
                    nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('sum',
                    action='store_const',
                    const=sum)

parser.add_argument('len',
                    action='store_const',
                    const=len)

args = parser.parse_args()
add = args.sum(args.integers)
length = args.len(args.integers)
average = add / length
print(average)
