# Source: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
def preOrder(root):
    if root != None:
        
        print(root.info, end = " ")
        preOrder(root.left)
        preOrder(root.right)
