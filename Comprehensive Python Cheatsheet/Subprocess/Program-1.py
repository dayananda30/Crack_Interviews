'''
Discussing all the args in subprocess.popen() and their usage:

syntax :
subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)


'''
import subprocess
import os
print("#=======================================================================")
print("# --- CWD- Current Working arguement ---")
print("#=======================================================================")
long_list = subprocess.Popen("dir", cwd=r'C:\\Users\\ddr\\Desktop\\Copy', stdout=subprocess.PIPE, shell=True)
output = long_list.communicate()
print(output)



print("#=======================================================================")
print("# --- Executable  arguement ---")
print("#=======================================================================")
launch_notepad = subprocess.Popen("abc.txt", executable=r"C:\\WINDOWS\\system32\\notepad.exe", stdout=subprocess.PIPE, shell=True)
#output = launch_notepad.communicate()
#print(output)



print("#=======================================================================")
print("# --- Close File Descriptors ---")
print("#=======================================================================")
f = open('Streaming_logs.py')
close_fd = subprocess.Popen("dir", shell=True, close_fds=True)
output = close_fd.communicate()
print(output)


print("#=======================================================================")
print("# --- Universal new lines ---")
print("# By Default, Universal_newlines=False(meaning input/output is accepted as bytes not as unicode string.)")
print("# if univaeral_newlines=False then for line in f.stdout: iterates over b'\\n' seperated lines)")
print("#=======================================================================")
f = open('Streaming_logs.py')
close_fd = subprocess.Popen("dir", shell=True, universal_newlines=True)
output = close_fd.communicate()
print(output)























