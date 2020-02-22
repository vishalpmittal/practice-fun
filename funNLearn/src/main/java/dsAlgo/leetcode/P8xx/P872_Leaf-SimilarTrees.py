"""
    Tag: tree

    Consider all the leaves of a binary tree.  From left to right order, 
    the values of those leaves form a leaf value sequence.

    For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
    https://leetcode.com/problems/leaf-similar-trees/

    Two binary trees are considered leaf-similar if their leaf value sequence is the same.

    Return true if and only if the two given trees with head nodes 
    root1 and root2 are leaf-similar.

    Note: Both of the given trees will have between 1 and 100 nodes.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeafSequence(r: TreeNode, seq: List[int]):
            if not r:
                return
            if not r.left and not r.right:
                seq.append(r.val)
            getLeafSequence(r.left, seq)
            getLeafSequence(r.right, seq)

        seq1, seq2 = [], []
        getLeafSequence(root1, seq1)
        getLeafSequence(root2, seq2)
        return seq1 == seq2


assert Solution().leafSimilar()
print('Tests Passed!!')
