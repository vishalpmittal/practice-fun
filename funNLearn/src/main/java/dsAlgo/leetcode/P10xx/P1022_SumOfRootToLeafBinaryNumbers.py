"""
    Tag: tree

    Given a binary tree, each node has value 0 or 1.  
    Each root-to-leaf path represents a binary number starting 
    with the most significant bit.  
    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this 
    could represent 01101 in binary, which is 13.

    For all leaves in the tree, consider the numbers represented 
    by the path from the root to that leaf.

    Return the sum of these numbers.

    Example 1: Input: [1,0,1,0,1,0,1] Output: 22
    Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

    Note:
    -  The number of nodes in the tree is between 1 and 1000.
    -  node.val is 0 or 1.
    -  The answer will not exceed 2^31 - 1.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.rtls = []

        def dfs(r: TreeNode, bs: int):
            if not r:
                return
            cs = r.val + bs*2
            if not r.left and not r.right:
                self.rtls.append(cs)
                return
            dfs(r.left, cs)
            dfs(r.right, cs)

        if not root:
            return -1
        if not root.left and not root.right:
            return root.val
        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return sum(self.rtls)

    def sumRootToLeaf(self, root, val=0):
        # similar but a little variant
        if not root:
            return 0
        val = val * 2 + root.val
        if root.left == root.right:
            return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)


TN = TreeNode
r = TN(1)
r.left, r.right = TN(0), TN(1)
r.left.left, r.left.right = TN(0), TN(1)
r.right.left, r.right.right = TN(0), TN(1)
assert Solution().sumRootToLeaf(r) == 22
print('Tests Passed!!')
