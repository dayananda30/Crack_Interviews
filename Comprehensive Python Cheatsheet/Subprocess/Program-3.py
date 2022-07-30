'''
This is a helper function which calls Program-2.py


'''
import subprocess

proc = subprocess.Popen(["python", "Program-2.py"])

while proc.returncode is None:
    proc.poll()
