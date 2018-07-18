class Node:
    def __init__(self,data,nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self,val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,val):
        self.nextNode = val

class LinkedList:
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def addNode(self,data):
        NewNode = Node(data,self.head)
        self.head = NewNode
        self.size = self.size + 1
        return True

    def getSize(self):
        return self.size


    def printNode(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.getNextNode()


    def findNode(self,val):
        self.val = val
        cur = self.head
        while cur:
            if cur.data == self.val:
                print("{} is exists".format(cur.data))
                return True
            cur = cur.getNextNode
        return False

    def removeNode(self,val):
        prev = None
        cur = self.head

        while cur:
            if cur.data == val:
                if prev:
                    prev.setNextNode(cur.getNextNode())
                else:
                    self.head = cur.getNextNode()
                return True

            prev = cur
            cur = cur.getNextNode()
        return False


n = LinkedList()
n.addNode(10)
n.addNode(20)
n.printNode()
print(n.getSize())
print("###################")
n.findNode(20)
n.addNode(30)
n.addNode(40)
n.addNode(50)
n.removeNode(50)
n.printNode()
