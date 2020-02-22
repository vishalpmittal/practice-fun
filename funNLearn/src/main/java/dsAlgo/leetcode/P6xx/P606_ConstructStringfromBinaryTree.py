"""
    Tag: tree, string

    You need to construct a string consists of parenthesis and integers 
    from a binary tree with the preorder traversing way.

    The null node needs to be represented by empty parenthesis pair "()". 
    And you need to omit all the empty parenthesis pairs that don't affect 
    the one-to-one mapping relationship between the string and the original binary tree.

    Example 1:  Input: Binary tree: [1,2,3,4]     Output: "1(2(4))(3)"
           1
         /   \
        2     3
       /    
      4     
    Explanation: Originallay it needs to be "1(2(4)())(3()())", 
    but you need to omit all the unnecessary empty parenthesis pairs. 
    And it will be "1(2(4))(3)".

    Example 2:  Input: Binary tree: [1,2,3,null,4]     Output: "1(2()(4))(3)"
           1
         /   \
        2     3
         \  
          4 
    Explanation: Almost the same as the first example, except we can't omit the 
    first parenthesis pair to break the one-to-one mapping relationship between 
    the input and the output.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        rs = '{}'.format(t.val)
        if not t.left and not t.right:
            return rs
        if t.left:
            rs += '(' + self.tree2str(t.left) + ')'
        else:
            rs += '()'
        if t.right:
            rs += '(' + self.tree2str(t.right) + ')'
        return rs


T1 = TreeNode(1)
T1.left, T1.right = TreeNode(2), TreeNode(3)
T1.left.left = TreeNode(4)

T2 = TreeNode(1)
T2.left, T2.right = TreeNode(2), TreeNode(3)
T2.left.right = TreeNode(4)

print(Solution().tree2str(T1))
print(Solution().tree2str(T2))

# assert Solution().solve_problem([], [])
print('Tests Passed!!')
