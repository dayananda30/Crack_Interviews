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
        del temp

    def insertAt(self,newNode,pos):

        if pos == 0:
            self.insertAtBeginning(newNode)
            return

        length = self.lengthofLinkedList()
        if pos > length:
            print("Invalid Position which exceeds the linked list length")
            import sys
            sys.exit()
        count = 0
        self.prev = None
        self.cur = self.head

        while True:
            if count < pos:
                self.prev = self.cur
                self.cur = self.cur.next
                count = count + 1
            elif count == pos:
                self.prev.next = newNode
                newNode.next = self.cur
                break


    def lengthofLinkedList(self):
        cur = self.head
        self.length = 0

        while cur is not None:
            self.length = self.length + 1
            cur = cur.next
        #print("The Length of the LinkedList is : ".format(self.length))
        return self.length

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
    firstNode = Node("10")
    linkedlist = LinkedList()

    secondnode = Node("20")

    thirdNode = Node("15")

    linkedlist.insertAtBeginning(firstNode)

    linkedlist.insertAtEnd(secondnode)

    linkedlist.insertAt(thirdNode,1)#linkedlist.insertAt(thirdNode, 0)

    fouthnode = Node(30)

    linkedlist.insertAtEnd(fouthnode)

    linkedlist.printNodes()

    #linkedlist.lengthofLinkedList()
