"""
For a binary tree,
write a program that can print to the path to each leaf node from the root:

                         7
                      /     \
                     1        2
                   /   \        \    
                (5)     6        (8)
                       /
                     (4)

Given the tree above as an example, the program should print the following:
                     
7 1 5
7 1 6 4
7 2 8
"""
from typing import List

class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left 
        self.right = right
        self.value = value 
        
    
def print_path_to_leaf(root:Node):
   
    def dfs(curr_node: Node, curr_path: str):
        # it's a leaf node
        if not curr_node.left and not curr_node.right:
            print(curr_path + " " + str(curr_node.value))
            
        if curr_node.left:
            dfs(curr_node.left, curr_path + " " + str(curr_node.value))
        
        if curr_node.right:
            dfs(curr_node.right, curr_path + " " + str(curr_node.value))
    
    dfs(root, "")


def print_path_to_leaf_list(root:Node):
    complete_list = []

    def dfs(curr_node: Node, curr_path: List[int]):
        # it's a leaf node
        if not curr_node.left and not curr_node.right:
            complete_list.append(curr_path)
            
        curr_path.append(curr_node.value)
        if curr_node.left:
            sub_path = curr_path.copy()
            dfs(curr_node.left, sub_path)
        
        if curr_node.right:
            sub_path = curr_path.copy()
            dfs(curr_node.right, sub_path)
    
    dfs(root, [])
    return complete_list
    

n5 = Node(value=5)
n4 = Node(value=4)
n8 = Node(value=8)
n6 = Node(value=6, left=n4)
n1 = Node(value=1, left=n5, right=n6)
n2 = Node(value=2, right=n8)
n7 = Node(value=7, left=n1, right=n2)
    
print_path_to_leaf(n7)
print(print_path_to_leaf_list(n7))
