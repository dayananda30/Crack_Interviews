"""
Creating Nodes , LinkedLists and adding the Nodes to the Linked at the END/Beginning. and displaying all the Node's Data

"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                else:
                    lastnode = lastnode.next
            lastnode.next = newNode

    def insertAtBeginning(self,newNode):
        temp = self.head
        self.head = newNode
        self.head.next = temp


    def printNodes(self):
        temp = self.head
        #print(temp.data)
        while True:
            if temp is not None:
                print(temp.data)
                temp = temp.next
            else:
                break

if __name__ == "__main__":
    firstNode = Node("firstNode")
    linkedlist = LinkedList()
    linkedlist.insertAtEnd(firstNode)

    secondnode = Node("Second Node")

    thirdNode = Node("Third Node")

    linkedlist.insertAtEnd(secondnode)

    linkedlist.insertAtEnd(thirdNode)

    new = Node("Head Node")

    linkedlist.insertAtBeginning(new)


    linkedlist.printNodes()
