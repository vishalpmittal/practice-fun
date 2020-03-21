"""
    tag: tree, recursive, bst

    Given a binary tree and a node, find inorder successor of this node. 
           20 
          /  \
         8    22
        / \    
       4   12
          /  \
        10    14  

    In order successor of 8 is 10, for 10 is 12 and for 14 is 20
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minValue(self, root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def inOrderSuccessor(root: Node, node: Node):
    if node.right != None:
        return minValue(node.right)

    succ = None
    while root != None:
        if node.data < root.data:
            succ = root
            root = root.left
        elif node.data > root.data:
            root = root.right
        else:
            break

    return succ
