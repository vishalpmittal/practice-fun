"""
Helper class for a tree's node
"""
from Queue import Queue


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def make_me_a_tree(list_of_nodes):
        """
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
        """
        ll = len(list_of_nodes)
        if list_of_nodes == None or ll == 0:
            return None

        rn = TreeNode(list_of_nodes[0])
        nq = Queue()
        nq.put(rn)
        cnp = 1  # child node pointer
        while nq.qsize > 0 and cnp < ll:
            curr_node = nq.get()
            if list_of_nodes[cnp]:
                lnode = TreeNode(list_of_nodes[cnp])
                curr_node.left = lnode
                nq.put(lnode)
            cnp += 1
            if cnp < ll and list_of_nodes[cnp]:
                rnode = TreeNode(list_of_nodes[cnp])
                curr_node.right = rnode
                nq.put(rnode)
            cnp += 1
        return rn

    def __str__(self):
        l = self.left.val if self.left else '_'
        r = self.right.val if self.right else '_'
        return '{} <- {} -> {}'.format(l, self.val, r)

    @staticmethod
    def tree2str(node):
        if not node:
            return ''
        ret = str(node)
        if node.left and (node.left.left or node.left.right):
            ret += '\n' + str(TreeNode.tree2str(node.left))
        if node.right and (node.right.left or node.right.right):
            ret += '\n' + str(TreeNode.tree2str(node.right))
        return ret

    def is_equal(self, node):
        if not node:
            return False
        if (self.val == node.val) and (
            bool(self.left) == bool(node.left)) and (
            bool(self.right) == bool(node.right)
        ):
            return True
        return False

    @staticmethod
    def is_tree_equal(rn1, rn2):
        """
        returns true if all the nodes are equal in the tree
        """
        if rn1 is None or rn2 is None:
            return rn1 == rn2

        return rn1.is_equal(rn2
            ) and TreeNode.is_tree_equal(rn1.left, rn2.left
            ) and TreeNode.is_tree_equal(rn1.right, rn2.right
        )
