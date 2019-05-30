"""
    Tag: tree

    Given a binary tree and a sum, find all root-to-leaf paths where each 
    path's sum equals the given sum.

    Note: A leaf is a node with no children.

    
    Example: Given the below binary tree and sum = 22,
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1

    Return:
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
"""
import os 
from tree_node import TreeNode as TN


def pathSum(root, sum):
    list_of_list = list()
    if root == None:
        return list_of_list
    ps_helper(root, sum, [], list_of_list)
    return list_of_list 


def ps_helper(root, sum, curr_list, list_of_list):
    if root == None:
        return
    curr_list.append(root.val)
    if root.left == None and root.right == None and root.val == sum:
        list_of_list.append(curr_list)
        return
    ps_helper(root.left, sum - root.val, list(curr_list), list_of_list)
    ps_helper(root.right, sum - root.val, list(curr_list), list_of_list)


def test_code():
    rn = TN.make_me_a_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    # print TN.tree2str(rn)
    print pathSum(rn, 22)
    # print "Tests Passed!!"


test_code()
