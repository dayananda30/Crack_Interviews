"""
os.chdir(<path>) # Changes the current working directory.
os.mkdir(<path>, mode=0o777) # Creates a directory. Mode is in octal.
shutil.copy(from, to) # Copies the file. 'to' can exist or be a dir.
shutil.copytree(from, to) # Copies the directory. 'to' must not exist.


os.rename(from, to) # Renames/moves the file or directory.
os.replace(from, to) # Same, but overwrites 'to' if it exists.
os.remove(<path>) # Deletes the file.
os.rmdir(<path>) # Deletes the empty directory.
shutil.rmtree(<path>) # Deletes the directory.
"""