"""
    tag: linked list

    Give a Linked List head node, return the head of a clone list. 
    The linked list nodes are nodes that have next nodes and can also 
    point to a random node in the list. 

    For Eg: input linked list
    1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

    Random Pointers
    1 -> 5
    2 -> 3
    4 -> 2
    4 -> None
    5 -> 3
    6 -> 4 (1st one)
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.random = None


# Random Pointer Linked List
class RMLinkedList:
    def __init__(self, head: Node):
        self.head = head

    def clone_llist(self) -> Node:
        old_node_to_cloned_node = {None: None}

        curr_n = self.head
        while curr_n is not None:
            old_node_to_cloned_node[curr_n] = Node(curr_n.val)
            curr_n = curr_n.next

        # on = old node, cn = current node
        for on, cn in old_node_to_cloned_node.items():
            cn.next = old_node_to_cloned_node[on.next]
            cn.random = old_node_to_cloned_node[on.random]

        return old_node_to_cloned_node[self.head]
