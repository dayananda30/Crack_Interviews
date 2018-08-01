
def display(string):
    size = len(string)
    n = 0
    for i in range(-1,(-size-1),-1):
        print("{}       {}".format(string[n],string[i]))
        n = n + 1


display("Dayananda")
