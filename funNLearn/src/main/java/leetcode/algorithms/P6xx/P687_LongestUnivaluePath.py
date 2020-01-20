"""
    Tag: tree

    Given a binary tree, find the length of the longest path where each node 
    in the path has the same value. This path may or may not pass through the root.

    The length of path between two nodes is represented by the number of 
    edges between them.

    Example 1:  Input:   Output: 2
                 5
                / \
               4   5
              / \   \
             1   1   5

    Example 2:  Input:   Output: 2
                 1
                / \
               4   5
              / \   \
             4   4   5

    Note: The given binary tree has not more than 10000 nodes. 
    The height of the tree is not more than 1000.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


TN = TreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def arrow_length(node):
            if not node:
                return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans


r = TN(5)
r.left, r.right = TN(4), TN(5)
r.left.left, r.left.right, r.right.right = TN(1), TN(1), TN(5)

r2 = TN(1)
r2.left, r2.right = TN(4), TN(5)
r2.left.left, r2.left.right, r2.right.right = TN(4), TN(4), TN(5)


assert Solution().longestUnivaluePath(r) == 2
assert Solution().longestUnivaluePath(r2) == 2
print('Tests Passed!!')
