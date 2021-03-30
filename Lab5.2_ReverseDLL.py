
# Source: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    
    currentNode = head
    temp = None
    while currentNode != None:
        
        temp = currentNode.prev
        
        currentNode.prev = currentNode.next
        currentNode.next = temp
        currentNode = currentNode.prev
        
        if temp != None:
            
            head = temp.prev
    return head
        
