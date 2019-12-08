"""
    Tag: tree, list
    
    Given a Binary Search Tree (BST), convert it to a Greater Tree such that 
    every key of the original BST is changed to the original key plus sum 
    of all keys greater than the original key in BST.

    Example:
    Input: The root of a Binary Search Tree like this:
                5
              /   \
            2     13

    Output: The root of a Greater Tree like this:
                18
              /   \
            20     13
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

    def convertBST_1(self, root):
        total = 0

        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
Solution().convertBST(root)
assert root.val == 18 and root.left.val == 20 and root.right.val == 13
print('Tests Passed!')
