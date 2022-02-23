"""
    tag: tree

    Given a tree, find that one swap that can convert it to a BST    
    #1                   10
    #               /        \
    #            15           5           
    #           /   \       /   \  
    #          4     7   14      17   swap 5 and 15
    
    #2                  10
    #               /        \
    #             5           14           
    #           /   \       /   \  
    #          4     7   15     17      swap 14 and 15
    
    #3                   10
    #               /       \
    #             5          15           
    #           /   \      /   \  
    #          4    17   14     7      swap 7 and 17
    
    #4                  14
    #               /        \
    #             5           13           
    #           /   \       /   \  
    #          4     7    12     10      swap 14 and 10
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def iot(root):
    iol = []

    def helper(cn):
        if not cn:
            return

        helper(cn.left)
        iol(cn)
        helper(cn.right)

    helper(root)
    return iol


def find_sort_pair(iol: List[TreeNode]):
    # Fist get the in order traversal of the tree
    # eg. [4, 15, 7, 10, 14, 5, 17] --> 1
    # for any such tree the pair should be two misplaced elements on the far corner of the list
    # eg. 15 and 5
    # find those and replace

    left = -1
    i = 0
    while i < len(iol) - 1 and left == -1:
        if iol[i].val > iol[i + 1].val:
            left = i
        i += 1

    j = len(iol) - 1
    right = -1
    while j > i and right == -1:
        if iol[j].val < iol[j - 1].val:
            right = j
        j -= 1

    if i != -1 and j != -1:
        iol[i].val, iol[j].val = iol[j].val, iol[i].val

