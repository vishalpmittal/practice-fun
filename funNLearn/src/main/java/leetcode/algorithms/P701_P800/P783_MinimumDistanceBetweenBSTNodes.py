"""
    Tag: tree

    Given a Binary Search Tree (BST) with the root node root, return the minimum 
    difference between the values of any two different nodes in the tree.

    Example : Input: root = [4,2,6,1,3,null,null]    Output: 1
    Explanation: Note that root is a TreeNode object, not an array.
    The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
              4
            /   \
           2     6
          / \    
         1   3  

    while the minimum difference in this tree is 1, it occurs between 
    node 1 and node 2, also between node 3 and node 2.

    Note:
    -  The size of the BST will be between 2 and 100.
    -  The BST is always valid, each node's value is an integer, and each 
    node's value is different.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans


T = TreeNode
r = T(4)
r.left, r.right = T(2), T(6)
r.left.left, r.left.right = T(1), T(3)
assert Solution().minDiffInBST(r) == 1

r = T(90)
r.left = T(69)
r.left.left, r.left.right = T(49), T(89)
r.left.left.right = T(52)
assert Solution().minDiffInBST(r) == 1

print('Tests Passed!!')
