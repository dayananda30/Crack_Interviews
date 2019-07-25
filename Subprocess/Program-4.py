'''
This is similar to Program-2 but witthout user interaction

'''


import subprocess,sys

proc = subprocess.Popen(["python", "Program-2.py"], stdin=subprocess.PIPE,)

proc.stdin.write("sajkbdjkhbsadba\n")
proc.stdin.write("saj kbdj khbs adba\n")
proc.stdin.write("sajkb djkh bsa dba\n")

while proc.returncode is None:
    i = sys.stdin.read(1)
    if i == 'exit':
        proc.stdin.close()
        break
    proc.stdout.write()


while proc.returncode is None:
    proc.poll()






