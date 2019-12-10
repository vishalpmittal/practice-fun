"""
    Tag: tree, design ds

    Given a n-ary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the 
    root node down to the farthest leaf node.

    Nary-Tree input serialization is represented in their level order traversal, 
    each group of children is separated by the null value (See examples).

    Example 1:  Input: root = [1,null,3,2,4,null,5,6]   Output: 3
    Example 2:  
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: 5

    Constraints:
    -  The depth of the n-ary tree is less than or equal to 1000.
    -  The total number of nodes is between [0, 10^4].
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif not root.children:
            return 1
        depth = set()
        for c in root.children:
            depth.add(1 + self.maxDepth(c))
        return max(depth)

    def maxDepth_iterative(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))
        return depth


print('Tests Passed!!')
