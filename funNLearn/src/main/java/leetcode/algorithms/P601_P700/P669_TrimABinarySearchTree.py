"""
    Tag: tree

    Given a binary search tree and the lowest and highest boundaries as L and R, 
    trim the tree so that all its elements lies in [L, R] (R >= L). You might 
    need to change the root of the tree, so the result should return the new 
    root of the trimmed binary search tree.

    Example 1: Input: L = 1, R = 2         Output:
               1                             1
              / \                             \
             0   2                             2

    Example 2: Input: L = 1, R = 3       Output: 
             3                           3
            / \                         / 
           0   4                       2   
            \                         /
             2                       1
            /
           1
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        return True
        if not root:
            return None
        if L > root.val:
            return self.trimBST(root.right, L, R)
        elif R < root.val:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


TN = TreeNode
r = TN(1)
r.left, r.right = TN(0), TN(2)
assert Solution().trimBST(r) == TN(1)
print('Tests Passed!!')
