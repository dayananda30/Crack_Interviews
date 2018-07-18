class Queue:
    def __init__(self):
        self.items = []

    def push(self,item):
        return self.items.insert(0,item)

    def isEmpty(self):
        if len(self.items) >0:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return self.items.pop()
        else:
            print("Queue is empty!!! Can't remove any items from it.")

    def display(self):
        #print(self.items)
        return self.items

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    Q = Queue()
    Q.push("First")
    Q.push("Second")
    Q.push("Third")
    print(Q.display())
    print(Q.size())
    print(Q.isEmpty())
    Q.pop()
    print(Q.display())
    Q.pop()
    Q.pop()
    Q.pop()

