# Python program to for tree traversals
# A class that represents an individual node in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):         # A function to do inorder tree traversal
    if root:
        printInorder(root.left)   # First recur on left child
        print(root.val)           # then print the data of node
        printInorder(root.right)  # now recur on right child

def printPostorder(root):   # A function to do postorder tree traversal
    if root:
        printPostorder(root.left)  # First recur on left child
        printPostorder(root.right)   # the recur on right child
        print(root.val)            # now print the data of node

def printPreorder(root):    # A function to do preorder tree traversal
    if root:
        print(root.val)      # First print the data of node
        printPreorder(root.left) # Then recur on left child
        printPreorder(root.right)  # Finally recur on right child

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal of binary tree is")
printPreorder(root)           # NLR

print("\nInorder traversal of binary tree is")
printInorder(root)            # LNR

print("\nPostorder traversal of binary tree is")
printPostorder(root)          # LRN
