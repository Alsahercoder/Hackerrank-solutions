#Source: https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
def inOrder(root):
    
    if root != None:
        
        inOrder(root.left)
        print(root.info, end = " ")
        inOrder(root.right)
