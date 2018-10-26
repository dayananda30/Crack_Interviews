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
        self.LinkedList1 = LinkedList1
        self.LinkedList2 = LinkedList2

        print(self.LinkedList1.head.data)
        print(self.LinkedList2.head.data)


        currentNode1 = LinkedList1.head
        currentNode2 = LinkedList2.head

        MergedLinkedList = LinkedList()

        while currentNode1 is not None and currentNode2 is not None:
            

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


    res = LinkedList()
    res.mergeLinkedLists(linkedlist1,linkedlist2)


