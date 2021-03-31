class Node:

    def __init__(self, data = None, next = None):

        self.data = data
        self.next = next
    
class LinkedList:

    def __init__(self):

        self.head = None
    
    def insertBegLL(self, payload):

        newNode = Node(payload)
        if self.head == None:

            self.head = newNode
            newNode.next = None
        else:

            temp = self.head    
            newNode.next = temp
            self.head = newNode

    def deleteBegLL(self):

        if self.head != None:
            temp = self.head
            print(self.head.data)
            self.head = self.head.next
            del(temp)
    
    def top(self):

        if self.head != None:
            print(self.head.data)
        else:
            return None

if __name__ == "__main__":

    tt = int(input())

    for i in range(0, tt):

        op = int(input())
        stack = LinkedList()

        for j in range(0, op):

            todo = input().split()
            if len(todo) == 2:

                stack.insertBegLL(int(todo[1]))

            elif todo[0] == "pop":

                stack.deleteBegLL()
            elif todo[0] == "top":

                stack.top()

