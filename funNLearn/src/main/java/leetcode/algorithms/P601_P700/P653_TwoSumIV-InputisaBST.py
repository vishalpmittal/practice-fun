"""
    Tag: tree

    Given a Binary Search Tree and a target number, return true 
    if there exist two elements in the BST such that their sum is equal 
    to the given target.

    Example 1:   Input: Target = 9,     Output: True
                5
               / \
              3   6
             / \   \
            2   4   7

    Example 2:   Input:  Target = 28,  Output: False
                 5
                / \
               3   6
              / \   \
             2   4   7
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False


TN = TreeNode
r = TN(5)
r.left, r.right = TN(3), TN(6)
r.left.left, r.left.right = TN(2), TN(4)
r.right.right = TN(7)

assert Solution().findTarget(r, 9)
assert not Solution().findTarget(r, 28)
print('Tests Passed!!')
