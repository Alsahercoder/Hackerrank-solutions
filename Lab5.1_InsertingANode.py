# Source: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
def sortedInsert(head, data):
    
    newNode = DoublyLinkedListNode(data)
    currentPtr = head
    
    # if the first node is already the greater than the data
    if head.data >= newNode.data:
        
        newNode.next = head
        newNode.next.prev = newNode
        head = newNode
        newNode.prev = None
        
        return head
    
    else:
        while currentPtr.next != None and currentPtr.next.data < data:
            
            currentPtr = currentPtr.next
            
        
        newNode.next = currentPtr.next
        if currentPtr.next != None: 
                newNode.next.prev = newNode 
  
        currentPtr.next =  newNode
        newNode.prev = currentPtr
        
    return head

