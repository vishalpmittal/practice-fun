"""
    tag: tree, recursive

    Give a root node find if binary tree is a Binary Search Tree

    Approach: 
    - every left node should be in between -inf to parent node value 
    - every right node should be in between parent node value and +inf
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkIfBST(root: Node) -> bool:
    ni = float("-inf")  # negative infinity
    pi = float("inf")  # positive infinity

    # node, lower bound, upper bound
    def dfs(nd, lb, ub):
        if not nd:
            return True
        if lb < nd.data < ub:
            return dfs(nd.left, ni, nd.data) and dfs(nd.right, nd.data, pi)
        return False

    return dfs(root, ni, pi)


R = Node(10)
R.left, R.right = Node(-10), Node(19)
R.left.left, R.left.right = Node(-20), Node(0)
R.right.left = Node(17)

assert checkIfBST(R)
print("Tests Passed!")
