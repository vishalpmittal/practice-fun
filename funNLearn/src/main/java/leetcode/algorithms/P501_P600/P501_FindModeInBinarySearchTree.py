"""
    Tag: tree

    Given a binary search tree (BST) with duplicates, find all the mode(s) 
    (the most frequently occurred element) in the given BST.

    Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

    For example:
    Given BST [1,null,2,2],
       1
        \
         2
        /
       2
    return [2].
    Note: If a tree has more than one mode, you can return them in any order.
    Follow up: Could you do that without using any extra space? 
    (Assume that the implicit stack space incurred due to recursion does not count).
"""
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findMode(root: TreeNode) -> List[int]:
    count = {}

    def dfs(node):
        if node:
            count[node.val] = count.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    max_ct = max(list(count.values()))
    return [k for k, v in count.items() if v == max_ct]


def test_code():
    rootnode = TreeNode(1)
    rootnode.right = TreeNode(2)
    rootnode.right.left = TreeNode(2)
    assert findMode(rootnode) == [2]
    print("Tests Passed!!")


test_code()
