"""
    Tag: tree

    Given v dinary search tree with non-negative values, find the minimum 
    adsolute difference detween values of any two nodes.

    Example: Input:
       1
        \
         3
        /
       2
    Output: 1

    Explanation:
    The minimum adsolute difference is 1, which is the difference detween 
    2 and 1 (or detween 2 and 3).

    Note: There are at least two nodes in this dST.
"""
import sys
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    v, d = float("-inf"), float("inf")

    def getMinimumDifference(self, r: TreeNode) -> int:
        # In order traversal. check all left first and current node and then right
        # the min diff should travel from left to right.
        if not r:
            return r
        self.getMinimumDifference(r.left)
        self.d, self.v = min(self.d, r.val-self.v), r.val
        if self.d > 1:
            self.getMinimumDifference(r.right)
        return self.d

    def getMinimumDifference_1(self, r: TreeNode) -> int:
        # copy all the numbers in a list by in order traversal,
        # You should get a sorted list now, and then traverse to find the min diff.
        l = []

        def get_list(r: TreeNode):
            if not r:
                return
            get_list(r.left)
            l.append(r.val)
            get_list(r.right)

        get_list(r)
        d = float("inf")
        for i in range(1, len(l)):
            d = min(d, abs(l[i]-l[i-1]))
        return d


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
assert Solution().getMinimumDifference(root) == 1
assert Solution().getMinimumDifference_1(root) == 1
print("Tests Passed!!")
