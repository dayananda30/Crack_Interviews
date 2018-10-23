#URL : https://www.youtube.com/watch?v=RhCGA4jlPmQ&list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo&index=2

# Create Nodes
# Create LinkedLists
# Add Nodes to LinkedLists
# Print Nodes



"""
Creating Nodes , LinkedLists and adding the Nodes to the Linked at the END. and displaying all the Node's Data


"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        #check whether linked list is empty or not?
        if self.head is None:
             self.head = newNode

        else:
            #self.head.next = newNode This will point first node point to last recently added node and all other middle nodes are skipped.
            lastNode = self.head

            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is Empty!")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next



if __name__ == '__main__':

    # Node which has data and the address of the next node
    # Node => data, next


    #fistNode.data => John
    #firstNode.next => None
    firstNode = Node("John")


    #Add this above Node to LinkedList.
    #First create a LinkedLisr
    linkedlist = LinkedList()

    linkedlist.insert(firstNode)


    #Second Node
    secondNode = Node("Ben")
    linkedlist.insert(secondNode)


    #Third Node
    thirdNode = Node("Mathew")
    linkedlist.insert(thirdNode)


    #printing all the Nodes
    linkedlist.printList()
