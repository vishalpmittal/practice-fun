"""
    tag: tree
    
    Given a binary tree, determine if it is a valid binary search tree (BST).
    
    Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
     
    Example 1:
        2
       / \
      1   3
    
    Input: [2,1,3]     Output: true
    
    Example 2:
        5
       / \
      1   4
         / \
        3   6
    
    Input: [5,1,4,null,null,3,6]    Output: false

    Explanation: The root node's value is 5 but its right child's value is 4.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_valid_BST(root: TreeNode) -> bool:
    """
        for ever node compare the curr value with a left bound and a right bound
        to recurse for the left node use existing left bound and curr_node as right bound
        to recurse for the right node use curr_node as left bound and existing right bound
    """
    if not root or (not root.left and not root.right):
        return True

    def helper(curr_node, lb, ub):
        if not curr_node:
            return True

        curr_val = curr_node.val

        if curr_val <= lb or curr_val >= ub:
            return False

        if not (
            helper(curr_node.left, lb, curr_val)
            and helper(curr_node.right, curr_val, ub)
        ):
            return False

        return True

    return helper(root, -1000, 1000)


def isValidBST_stack(self, root):
    """
        same as recursive just using stack.
    """
    if not root:
        return True

    stack = [
        (root, float("-inf"), float("inf")),
    ]
    while stack:
        root, lower, upper = stack.pop()
        if not root:
            continue
        val = root.val
        if val <= lower or val >= upper:
            return False
        stack.append((root.right, val, upper))
        stack.append((root.left, lower, val))
    return True


def isValidBST_InOrder(self, root):
    """
        do an inorder traversal. and if any element found which is not in order
        return false. 
    """
    stack, inorder = [], float("-inf")

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        # If next element in inorder traversal is smaller than the previous one
        # that's not BST.
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right

    return True


T = TreeNode
t1, t3 = T(1), T(3)
t2 = T(2)
t2.left, t2.right = t1, t3

n_1, n6, n1, n7, n5 = T(-1), T(6), T(1), T(7), T(5)
n1.left, n1.right = n_1, n6
n5.left, n5.right = n1, n7

assert is_valid_BST(t2)
assert not is_valid_BST(n5)
print("Tests Passed!")

