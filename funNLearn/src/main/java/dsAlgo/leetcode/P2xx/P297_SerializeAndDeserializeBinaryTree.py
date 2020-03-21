"""
    tag: tree

    Serialization is the process of converting a data structure or object into 
    a sequence of bits so that it can be stored in a file or memory buffer, or 
    transmitted across a network connection link to be reconstructed later in 
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no 
    restriction on how your serialization/deserialization algorithm should work. 
    You just need to ensure that a binary tree can be serialized to a string and 
    this string can be deserialized to the original tree structure.

    Example: You may serialize the following tree:
      1
     / \
    2   3
       / \
      4   5
    as "[1,2,3,null,null,4,5]"
    
    Clarification: The above format is the same as how LeetCode serializes a binary 
    tree. You do not necessarily need to follow this format, so please be creative 
    and come up with different approaches yourself.

    Note: Do not use class member/global/static variables to store states. 
    Your serialize and deserialize algorithms should be stateless.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        def rserialize(root, string):
            # check base case
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, "")

    def deserialize(self, data):
        def rdeserialize(l):
            if l[0] == "None":
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(",")
        root = rdeserialize(data_list)
        return root


T = TreeNode
R = T(1)
R.left, R.right = T(2), T(3)
R.right.left, R.right.right = T(4), T(5)
ser_str = "1,2,None,None,3,4,None,None,5,None,None,"
assert Codec().serialize(R) == ser_str
assert Codec().deserialize(ser_str).val == 1
