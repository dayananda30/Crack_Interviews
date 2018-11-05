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


    def mergeLinkedLists(self, LinkedList1, LinkedList2):
        self.currentNode1 = LinkedList1.head
        self.currentNode2 = LinkedList2.head

        while True:

            if self.currentNode1 is None:
                mergeList.insertAtEnd(self.currentNode2)
                break

            if self.currentNode2 is None:
                mergeList.insertAtEnd(self.currentNode1)
                break

            if self.currentNode1.data < self.currentNode2.data:
                curFirstNext = self.currentNode1.next
                self.currentNode1.next = None
                mergeList.insertAtEnd(self.currentNode1)
                self.currentNode1 = curFirstNext

            else:
                curSecondNext = not self.currentNode2.next
                self.currentNode2.next = None
                mergeList.insertAtEnd(self.currentNode2)
                self.currentNode2 = curSecondNext


    def printNodes(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


if __name__ == '__main__':
    firstNode = Node("1")
    linkedlist1 = LinkedList()
    linkedlist1.insertAtBeginning(firstNode)
    secondNode = Node("3")
    linkedlist1.insertAtEnd(secondNode)
    thirdNode = Node("4")
    linkedlist1.insertAtEnd(thirdNode)
    linkedlist1.printNodes()


    firstNode = Node("2")
    linkedlist2 = LinkedList()
    linkedlist2.insertAtBeginning(firstNode)
    secondNode = Node("7")
    linkedlist2.insertAtEnd(secondNode)
    thirdNode = Node("9")
    linkedlist2.insertAtEnd(thirdNode)
    linkedlist2.printNodes()
    print "##########"


    mergeList = LinkedList()
    mergeList.mergeLinkedLists(linkedlist1,linkedlist2)

    mergeList.printNodes()


