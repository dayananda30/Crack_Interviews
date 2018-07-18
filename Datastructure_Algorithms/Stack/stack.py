class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) != 0:
            return False
        else:
            return True

    def push(self,data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def display(self):
        print(self.items)

    def size(self):
        return len(self.items)



if __name__ == '__main__':
    s = Stack()
    print s.isEmpty()
    s.push(10)
    s.push(20)
    s.display()
    print s.isEmpty()
    print(s.size())
    print s.pop()
    print(s.display())
