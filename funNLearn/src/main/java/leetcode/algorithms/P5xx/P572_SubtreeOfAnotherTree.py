"""
    Tag: tree

    Given two non-empty binary trees s and t, check whether tree t has exactly 
    the same structure and node values with a subtree of s. A subtree of s is 
    a tree consists of a node in s and all of this node's descendants. 
    The tree s could also be considered as a subtree of itself.

    Example 1: Given tree s:       Given tree t:
                     3                     4       
                    / \                   / \       
                   4   5                 1   2        
                  / \                        
                 1   2                        
    Return true, because t has the same structure and node values with a subtree of s.

    Example 2: Given tree s:   Given tree t:
                        3                 4    
                       / \               / \     
                      4   5             1   2      
                     / \                  
                    1   2                  
                        /                  
                       0                  
    Return false.
"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isMatch(self, s: TreeNode, t: TreeNode) -> bool:
        if not(s and t):
            return s is t
        return (s.val == t.val and
                self.isMatch(s.left, t.left) and
                self.isMatch(s.right, t.right))

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isMatch(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


print("Tests Passed!!")
