"""
    Tag: tree

    In a binary tree, the root node is at depth 0, and
    children of each depth k node are at depth k+1.
    Two nodes of a binary tree are cousins if they have the
    same depth, but have different parents.
    We are given the root of a binary tree with unique values,
    and the values x and y of two different nodes in the tree.
    Return true if and only if the nodes corresponding to the
    values x and y are cousins.

    Example 1: Input: root = [1,2,3,4], x = 4, y = 3 Output: false
    Example 2: Input: root = [1,2,3,null,4,null,5], x = 5, y = 4 Output: true
    Example 3: Input: root = [1,2,3,null,4], x = 2, y = 3 Output: false

    Note:
    -  The number of nodes in the tree will be between 2 and 100.
    -  Each node has a unique integer value from 1 to 100.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.xd, self.yd, self.xp, self.yp = -1, -2, None, None

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def bfs(r: TreeNode, cd: int):
            if not r:
                return

            if r.left:
                if r.left.val == x:
                    self.xd, self.xp = cd+1, r.val
                elif r.left.val == y:
                    self.yd, self.yp = cd+1, r.val
                bfs(r.left, cd+1)
            if r.right:
                if r.right.val == x:
                    self.xd, self.xp = cd+1, r.val
                elif r.right.val == y:
                    self.yd, self.yp = cd+1, r.val
                bfs(r.right, cd+1)

        if not root or root.val == x or root.val == y:
            return False
        bfs(root, 0)
        return self.xd == self.yd and self.xp != self.yp


TN = TreeNode
r = TN(1)
r.left, r.right = TN(2), TN(3)
r.left.right, r.right.right = TN(4), TN(5)
assert Solution().isCousins(r, 4, 5)
print('Tests Passed!!')
