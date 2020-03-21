"""
    tag: tree

    Given a binary tree
         1
        /  \
       2    3
      / \  / \
     4  5  6  7
       / \     \
      8   9    10
               / \
              11  12

    Print output as 1,2,3,7,6,5,4,8,9,10,12,11
"""
from typing import List


class TN:  # treenode class
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_ziczac_levels(RN: TN) -> List[int]:
    if not RN:
        return

    Q, ans_list, order = [RN], [], 0

    while len(Q) > 0:
        temp_ans = []
        num_level_elements = len(Q)
        for _ in range(num_level_elements):
            curr_node = Q.get()
            temp_ans.append(curr_node.val)
            if curr_node.left:
                Q.append(curr_node.left)
            if curr_node.right:
                Q.append(curr_node.right)

        if order == 0:
            ans_list.extend(temp_ans)
        else:
            ans_list.extend(temp_ans[::-1])
        order = 0 if order == 1 else 1

    return ans_list
