"""
    Implement a function to store a tree to a string so that it can be later restored.
    Use case: how to send a binary tree through a network so the other party can reconstruct the same tree.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node, s=""):
    """
        recursive DFS, go to the left most first and then right most. 
        add # for nones. 
              3 
           2    6
         1    4   7 
        serialized string: "3 2 1 # # # 6 4 # # 7 # #"
    """
    if(not node):
        s += "# "
        return s
    s += (str(node.val)+" ")
    s = serialize(node.left, s=s)
    s = serialize(node.right, s=s)
    return s

def deserialize_str_manip(s:str) -> Node:
    """
        string manipulation way. lot of new strings created.
        recursively traverse through each value. add left first and then right. 
        for # add None and return. 
    """
    def helper(curr_str):
        if not curr_str or curr_str[0] == '#':
            return curr_str, None

        curr_node = Node(curr_str[0])
        curr_str, curr_node.left = helper(curr_str[2:])
        curr_str, curr_node.right = helper(curr_str[2:])
        
        return curr_str, curr_node
            
    return helper(s)[1]

i = 0
def deserialize(s):
    """
        use a global index i to know the next value.
        more efficient
    """
    global i
    if s[i] == "#":
            i += 2
        return None

    node = Node(s[i])
    i += 2
    node.left = deserialize(s)
    node.right = deserialize(s)
    return node

n1 = Node(1)
n4 = Node(4)
n7 = Node(7)
n2 = Node(2, left=n1)
n6 = Node(6, left=n4, right=n7)
rn = Node(3, left=n2, right=n6)

ser_string=serialize(rn)
print(f'"{ser_string}"')
root_node = deserialize(ser_string)
new_ser_string= serialize(root_node)
print(f'"{new_ser_string}"')
