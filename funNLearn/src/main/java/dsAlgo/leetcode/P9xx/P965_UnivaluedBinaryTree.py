"""
    Tag: tree

    A binary tree is univalued if every node in the tree has the same value.
    Return true if and only if the given tree is univalued.

    Example 1: Input: [1,1,1,1,1,null,1] Output: true
    Example 2: Input: [2,2,2,5,2] Output: false

    Note:
    The number of nodes in the given tree will be in the range [1, 100].
    Each node's value will be an integer in the range [0, 99].
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        left_correct = (not root.left or root.val == root.left.val
                        and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                         and self.isUnivalTree(root.right))
        return left_correct and right_correct


assert Solution().isUnivalTree()
print('Tests Passed!!')
