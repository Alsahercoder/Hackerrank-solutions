class Node:

    def __init__(self, data = None, prev = None, next = None):

        self.data = data
        self.prev = prev
        self.next = next
    
class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None
    
    def enqueue(self, payload):

        newNode = Node(payload)
        if self.head == None:

            newNode.prev = None
            self.head = newNode
            newNode.next = None
            self.tail = newNode
        else:

            temp = self.head
            self.head.prev = newNode    
            newNode.next = temp
            self.head = newNode

    def dequeue(self):

        if self.head == self.tail != None:
            
            print(self.tail.data)
            singleNode = self.head
            del(singleNode)
            self.head = None
            self.tail = None

        else:
            print(self.tail.data)
            newEndNode = self.tail.prev
            newEndNode.next = None
            curEndNode = self.tail
            del(curEndNode)
            self.tail = newEndNode
   
    def front(self):

        if self.tail != None:
            print(self.tail.data)
        else:
            return None

if __name__ == "__main__":

    tt = int(input())

    for i in range(0, tt):

        op = int(input())
        queue = LinkedList()

        for i in range(0, op):

            todo = input().split()
            if len(todo) == 2:

                queue.enqueue(int(todo[1]))

            elif todo[0] == "dequeue":

                queue.dequeue()
            elif todo[0] == "front":

                queue.front()

