"""
    tag: tree, serialize

    Implement a function to store a binary tree to a string so that it can be later restored.
    Use case: how to send a binary tree through a network so the other party can reconstruct the same tree.

             3
        2        6
     1         4    7

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_preorder(n:Node, s: str="") -> str:
    if(not n):
        return s

    s += " " + str(n.val)
    s = get_preorder(n.left, s)
    s = get_preorder(n.right, s)
    return s

def get_inorder(n:Node, s: str="") -> str:
    if(not n):
        return s
    
    s = get_inorder(n.left, s)
    s += " " + str(n.val)
    s = get_inorder(n.right, s)
    return s

def get_postorder(n:Node, s: str="") -> str:
    if(not n):
        return s
    s = get_postorder(n.left, s)
    s = get_postorder(n.right, s)
    s += " " + str(n.val)
    return s


def serialize(root: Node) -> str:
    """Serialize a binary tree to a string using preorder with null markers.

    Format: values separated by spaces, nulls represented by '#'.
    This works for any binary tree (not only BSTs).
    """
    tokens = []

    def helper(node: Node):
        if node is None:
            tokens.append('#')
            return
        tokens.append(str(node.val))
        helper(node.left)
        helper(node.right)

    helper(root)
    return ' '.join(tokens)


def deserialize(data: str) -> Node:
    """Deserialize string produced by `serialize` back into a binary tree."""
    if not data:
        return None

    tokens = iter(data.split())

    def helper():
        try:
            val = next(tokens)
        except StopIteration:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node

    return helper()


if __name__ == "__main__":
    n1 = Node(1)
    n4 = Node(4)
    n7 = Node(7)
    n2 = Node(2, left=n1)
    n6 = Node(6, left=n4, right=n7)
    rn = Node(3, left=n2, right=n6)

    print (get_inorder(rn))
    print (get_preorder(rn))
    print (get_postorder(rn))
    searialized_tree = serialize(rn)
    print (searialized_tree)
    print (serialize(deserialize(searialized_tree)))
