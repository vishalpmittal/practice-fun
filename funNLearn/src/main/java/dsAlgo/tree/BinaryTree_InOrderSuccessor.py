"""
    tag: tree, recursive

    Given a binary tree and a node, find inorder successor of this node. 
            1
          /  \
         2    3
        / \    \
       4   5    6

    In order successor of 4 is 5, for 5 is 1 and so on...
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

next = None


def inorderSuccessor(root, target_node):
    global next
    if root == None:
        return
    inorderSuccessor(root.right, target_node)

    # if target node found, then enter this condition
    if root.data == target_node.data:
        # this will be true to the last node in inorder traversal i.e., rightmost node.
        if next == None:
            print("inorder successor of", root.data, " is: None")
        else:
            print("inorder successor of", root.data, "is:", next.data)

    next = root
    inorderSuccessor(root.left, target_node)

