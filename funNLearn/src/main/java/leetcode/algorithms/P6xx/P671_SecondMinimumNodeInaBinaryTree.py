"""
    Tag: tree

    Given a non-empty special binary tree consisting of nodes with the non-negative 
    value, where each node in this tree has exactly two or zero sub-node. If the node 
    has two sub-nodes, then this node's value is the smaller value among its two 
    sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val)
    always holds.

    Given such a binary tree, you need to output the second minimum value in the 
    set made of all the nodes' value in the whole tree.

    If no such second minimum value exists, output -1 instead.

    Example 1: Input:        Output: 5
                2
               / \
              2   5
                 / \
                5   7
    Explanation: The smallest value is 2, the second smallest value is 5.
    

    Example 2: Input:         Output: -1
                2
               / \
              2   2
    Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root):
        def dfs(node):
            if node:
                uniques.add(node.val)
                dfs(node.left)
                dfs(node.right)

        uniques = set()
        dfs(root)

        min1, ans = root.val, float('inf')
        for v in uniques:
            if min1 < v < ans:
                ans = v

        return ans if ans < float('inf') else -1

    def findSecondMinimumValue_1(self, root: TreeNode) -> int:
        min1, self.ans = root.val, float('inf')

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1


TN = TreeNode
r = TN(2)
r.left, r.right = TN(2), TN(5)
r.right.left, r.right.right = TN(5), TN(7)
assert Solution().findSecondMinimumValue(r) == 5
assert Solution().findSecondMinimumValue_1(r) == 5

r = TN(2)
r.left, r.right = TN(2), TN(2)
assert Solution().findSecondMinimumValue(r) == -1
assert Solution().findSecondMinimumValue_1(r) == -1
print('Tests Passed!!')
