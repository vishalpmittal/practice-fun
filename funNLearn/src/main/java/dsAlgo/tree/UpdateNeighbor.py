"""
    tag: tree

    Given a tree that has three next pointers
    left, right and neighbor, but the neighbor pointer is not set
    Given the root node of the tree update the neighbor node

        1
       / \
      2   3
     /   / \
    4   5   6

    Here is what the out put should look like 
         1 -> NULL  
       /  \
      2 -> 3 -> NULL 
     /    /  \     
    4 -> 5 -> 6 -> NULL
"""


class TN:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.ngbr = None

    def __str__(self):
        return "({}, L:{}, R:{}, N:{})".format(
            self.val,
            self.left.val if self.left else "",
            self.right.val if self.right else "",
            self.ngbr.val if self.ngbr else "",
        )

    def print_tree(self):
        print(str(self))
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


def fill_neighbors(root: TN):
    """
        idea is to create a level list like 
        [[1], [2, 3], [4, 5, 6]]
        then point node at index i to node at i+1
    """
    if not root or (not root.left and root.right):
        return

    level_list = []

    def util(curr_node: TN, curr_level: int):
        if not curr_node:
            return

        while len(level_list) < curr_level + 1:
            level_list.append([])

        level_list[curr_level].append(curr_node)
        util(curr_node.left, curr_level + 1)
        util(curr_node.right, curr_level + 1)

    util(root, 0)
    # [[1], [2, 3], [4, 5, 6]]
    for level in level_list:
        for indx in range(1, len(level)):
            level[indx - 1].ngbr = level[indx]


def fill_neighbors2(root: TN):
    """
        idea is to create a level list like, 
        [1, 2, 4]
        instead of keeping list of lists just keep the las node visited at that level 
        and point last_node_at_level.ngbr -> curr_node and then replace the last_node_at_level 
        in the list with curr_node

        [1, 2, 4] -> [1, 3, 4]  -> [1, 3, 5] -> [1, 3, 6]
    """
    if not root or (not root.left and root.right):
        return

    level_list = []

    def util2(curr_node: TN, curr_level: int):
        if not curr_node:
            return

        if len(level_list) < curr_level + 1:
            level_list.append(curr_node)
        else:
            level_list[curr_level].ngbr = curr_node
            level_list[curr_level] = curr_node

        util2(curr_node.left, curr_level + 1)
        util2(curr_node.right, curr_level + 1)

    util2(root, 0)


n4, n5, n6 = TN(4), TN(5), TN(6)
n2 = TN(2, left=n4)
n3 = TN(3, left=n5, right=n6)
n1 = TN(1, left=n2, right=n3)
# n1.print_tree()
# fill_neighbors(n1)
fill_neighbors2(n1)
n1.print_tree()
