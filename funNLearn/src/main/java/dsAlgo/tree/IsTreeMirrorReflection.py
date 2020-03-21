"""
    tag: tree
    given a binary tree, create a mirror reflection of the tree
"""


class TreeNode:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def mirror_reflection(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root

        new_left = self.mirror_reflection(root.right)
        new_right = self.mirror_reflection(root.left)
        root.left, root.right = new_left, new_right

        return root


T = TreeNode
r = T(1)
r.left, r.right = T(2), T(3)
r.left.left, r.left.right = T(4), T(5)
r.right.left, r.right.right = T(6), T(7)

r = Solution().mirror_reflection(r)
assert r.left.val == 3 and r.right.val == 2
assert r.left.left.val == 7 and r.left.right.val == 6
assert r.right.left.val == 5 and r.right.right.val == 4
print("Tests passed!!")
