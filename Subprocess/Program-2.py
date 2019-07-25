'''
This program keep polling data from standard input (keyboard) using iter
It keep polls the user input until it finds exit keyboard.

program-3 implemented to trigger this program
'''
import os,sys


print("What is your name?")

for name in iter(sys.stdin.readline,''):
    name = name[:-1]
    if name == 'exit':
        break
    print("Well how do you do {0}?".format(name))
    print("What's your name?")

