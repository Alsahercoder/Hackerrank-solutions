# Source: https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
def postOrder(root):
    
    if root != None:
        
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end = " ")
