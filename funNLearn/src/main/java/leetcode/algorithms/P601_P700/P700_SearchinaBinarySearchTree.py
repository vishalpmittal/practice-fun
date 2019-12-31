"""
    Tag: tree

    Given the root node of a binary search tree (BST) and a value. 
    You need to find the node in the BST that the node's value equals the 
    given value. Return the subtree rooted with that node. If such node 
    doesn't exist, you should return NULL.

    For example,  Given the tree: and num=2
            4
           / \
          2   7
         / \
        1   3

    You should return this subtree:

          2     
         / \   
        1   3
    In the example above, if we want to search the value 5, since there 
    is no node with value 5, we should return NULL.

    Note that an empty tree is represented by NULL, therefore you would see the 
    expected output (serialized tree format) as [], not null.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root

        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)


r = TreeNode(4)
r.left, r.right = TreeNode(2), TreeNode(7)
r.left.left, r.left.right = TreeNode(1), TreeNode(3)
assert Solution().searchBST(r, 2).val == 2
assert Solution().searchBST(r, 5) == None
print('Tests Passed!!')
