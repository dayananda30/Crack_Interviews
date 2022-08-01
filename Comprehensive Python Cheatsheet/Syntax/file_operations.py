try:
    with open("arguments.py", mode="r", encoding="utf8") as fd:
        print(fd.name) # prints filename
        print(fd.read())
        print(fd.readlines()) # return file contents in a list.
        print(fd.readline(10)) # reads only that many characters
except FileNotFoundError:
    print("File Not Found")

