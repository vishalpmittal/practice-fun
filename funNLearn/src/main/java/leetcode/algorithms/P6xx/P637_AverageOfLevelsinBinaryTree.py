"""
    Tag: tree

    Given a non-empty binary tree, return the average value of the
    nodes on each level in the form of an array.
    Example 1: Input:,   Output: [3, 14.5, 11]
             3
            / \
           9  20
             /  \
            15   7

    Explanation:
    The average value of nodes on level 0 is 3, on level 1 is 14.5, and on
    level 2 is 11. Hence return [3, 14.5, 11].

"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        info = []

        def dfs(node, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]


r = TreeNode(3)
r.left, r.right = TreeNode(9), TreeNode(20)
r.right.left, r.right.right = TreeNode(15), TreeNode(7)
assert Solution().averageOfLevels(r) == [3, 14.5, 11]
print('Tests Passed!!')
