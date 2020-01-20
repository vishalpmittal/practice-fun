"""
    Tag: tree

    Given two binary trees and imagine that when you put one of them to cover the other, 
    some nodes of the two trees are overlapped while the others are not.

    You need to merge them into a new binary tree. The merge rule is that if two 
    nodes overlap, then sum node values up as the new value of the merged node. 
    Otherwise, the NOT null node will be used as the node of new tree.

    Example 1:        Input:                        Output: 
	        Tree 1           Tree 2               Merged tree:   
              1                  2             	     3                
             / \                / \            	    / \                
            3   2              1   3           	   4   5             
           /                    \   \          	  / \   \             
          5                      4   7         	 5   4   7         

    Note: The merging process must start from the root nodes of both trees.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        s = 0
        n_t1_l = n_t1_r = n_t2_l = n_t2_r = None
        if t1 and not t2:
            s, n_t1_l, n_t1_r = t1.val, t1.left, t1.right
        elif t2 and not t1:
            s, n_t2_l, n_t2_r = t2.val, t2.left, t2.right
        else:
            s = t1.val + t2.val
            n_t1_l, n_t1_r = t1.left, t1.right
            n_t2_l, n_t2_r = t2.left, t2.right

        new_node = TreeNode(s)
        new_node.left = self.mergeTrees(n_t1_l, n_t2_l)
        new_node.right = self.mergeTrees(n_t1_r, n_t2_r)
        return new_node

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # Same as above but Optimized
        if not t1 and not t2:
            return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans


print('Tests Passed!!')
