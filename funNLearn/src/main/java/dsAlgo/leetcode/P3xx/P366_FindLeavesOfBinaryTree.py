"""
    Tag: tree

    Given a binary tree, collect a tree's nodes as if you were doing this: 
    Collect and remove all leaves, repeat until the tree is empty.
    
    Example: [1,2,3,4,5]
                 1
                / \
               2   3
              / \     
             4   5    
    Output: [[4,5,3],[2],[1]]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.leaves = []

        def dfs(nd: TreeNode) -> int:
            if not nd:
                return -1

            depth = max(dfs(nd.left), dfs(nd.right)) + 1
            while len(self.leaves) < depth + 1:
                self.leaves.append([])
            self.leaves[depth].append(nd.val)
            return depth

        dfs(root)
        return self.leaves


T = TreeNode
r = T(1)
r.left, r.right = T(2), T(3)
r.left.left, r.left.right = T(4), T(5)
assert Solution().findLeaves(r) == [[4, 5, 3], [2], [1]]
print('Tests Passed!!')
