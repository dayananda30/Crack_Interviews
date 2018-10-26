class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,newNode):
        if self.head is None:
            self.head = newNode


    def insertAtEnd(self,newNode):
        cur = self.head
        while True:
            if cur.next is None:
                cur.next = newNode
                break
            cur = cur.next

    def deleteNode(self,pos):
        count = 0
        prev = None
        cur = self.head
        while cur.next is not None:
            if count == pos:
                print("I am here")
                prev.next = cur.next
                del cur
                break
            prev = cur
            cur = cur.next
            count = count + 1



    def printNodes(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


if __name__ == '__main__':
    firstNode = Node("one")

    linkedlist = LinkedList()


    linkedlist.insertAtBeginning(firstNode)

    secondNode = Node("Two")
    linkedlist.insertAtEnd(secondNode)


    thirdNode = Node("Third")
    linkedlist.insertAtEnd(thirdNode)

    fouthNode = Node("Fouth")
    linkedlist.insertAtEnd(fouthNode)

    print("After Deleting..... ")
    linkedlist.printNodes()

    linkedlist.deleteNode(2)

    print("After Deleting....")
    linkedlist.printNodes()

