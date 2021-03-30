# Source : https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
                
        if self.root == None:
            
            self.root = Node(val)
        
        else:
            ptr = self.root
            parentPtr = ptr
            while ptr != None:
                
                if val < ptr.info:
                    
                    parentPtr = ptr
                    ptr = ptr.left
                elif val >= ptr.info:
                    
                    parentPtr = ptr
                    ptr = ptr.right
            
            if val < parentPtr.info:
                
                parentPtr.left = Node(val)
            
            else:
                parentPtr.right = Node(val)
        
        return self.root
                
        
        #Enter you code here.

