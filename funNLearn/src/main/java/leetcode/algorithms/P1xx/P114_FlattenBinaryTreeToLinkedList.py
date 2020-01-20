"""
    Tag: tree,linked list
    Given a binary tree, flatten it to a linked list in-place.

    For example, given the following tree:

        1
       / \
      2   5
     / \   \
    3   4   6
    The flattened tree should look like:
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
"""

from tree_node import TreeNode as TN


def flatten(root):
    """
    recursive.
    """
    if root:
        flatten(root.left)
        flatten(root.right)
        p = root.left
        if p:
            while p.right:
                p = p.right
            p.right = root.right
            root.right = root.left
            root.left = None


def flatten_iterative(root):
    """
    Iterative solution based on pre order tree traversal
    """
    if not root: return
    
    stck, pre = [root], None
    while stck:
        poped_node = stck.pop()
        if pre:
            pre.left = None
            pre.right = poped_node
        pre = poped_node

        if poped_node.right: stck.append(poped_node.right)
        if poped_node.left: stck.append(poped_node.left)


def test_code():
    rn1 = TN.make_me_a_tree([1, 2, 5, 3, 4, None, 6])
    res_rn = TN.make_me_a_tree(
            [1, None, 2, None, 3, None, 4, None, 5, None, 6 ]
        )
    flatten(rn1)
    assert TN.is_tree_equal(rn1, res_rn)
    
    rn2 = TN.make_me_a_tree([1, 2, 5, 3, 4, None, 6])
    flatten_iterative(rn2)
    assert TN.is_tree_equal(rn1, rn2)
    print ('Tests Passed!!')


test_code()