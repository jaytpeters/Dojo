class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLList:
    def __init__(self, node = None):
        self.head = node
    def addNode(self, node):
        if self.head == None:
            self.head = node
        else:
            curNode = self.head
            while curNode.next != None:
                curNode = curNode.next
            curNode.next = node
    def printAllValues(self):
        if self.head != None:
            curNode = self.head
            while curNode.next != None:
                print("Value: " + str(curNode.value))
                curNode = curNode.next
            print("Value:  " + str(curNode.value))
        else:
            print("No Nodes")
    def removeNode(self, val):
        if self.head != None:
            curNode = self.head
            if curNode.value == val:
                if curNode.next != None:
                    self.head = curNode.next
                else:
                    self.head = None
            else:
                while curNode.next != None and curNode.next.value != val:
                    curNode = curNode.next
                if curNode.next == None:
                    print("Node not found")
                else:
                    if curNode.next.next == None:
                        curNode.next = None
                    else:
                        curNode.next = curNode.next.next

newNode = Node(5)
list = SLList(newNode)
newNode2 = Node(7)
list.addNode(newNode2)
newNode3 = Node(9)
list.addNode(newNode3)
newNode4 = Node(1)
list.addNode(newNode4)
list.removeNode(9)
list.removeNode(5)
list.removeNode(1)
list.printAllValues()


            
                