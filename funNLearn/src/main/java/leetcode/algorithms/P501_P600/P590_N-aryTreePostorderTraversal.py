"""
    Tag: tree, array

    Given an n-ary tree, return the postorder traversal of its nodes' values.
    Nary-Tree input serialization is represented in their level order traversal, 
    each group of children is separated by the null value (See examples).

    Follow up:
    Recursive solution is trivial, could you do it iteratively?

    Example 1: Input: root = [1,null,3,2,4,null,5,6] Output: [5,6,3,2,4,1]

    Example 2:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
    
    Constraints:
    -  The height of the n-ary tree is less than or equal to 1000
    -  The total number of nodes is between [0, 10^4]
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        po_list = []
        if root.children:
            for child in root.children:
                po_list.extend(self.postorder(child))
        po_list.append(root.val)
        return po_list

    def postorder_iterative(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            if root.children:
                for c in root.children:
                    stack.append(c)
        return output[::-1]


root = Node(1)
n3 = Node(3)
n3.children = [Node(5), Node(6)]
root.children = [n3, Node(2), Node(4)]

assert Solution().postorder(root) == [5, 6, 3, 2, 4, 1]
assert Solution().postorder_iterative(root) == [5, 6, 3, 2, 4, 1]
print("Tests Passed!!")
