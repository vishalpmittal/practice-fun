"""
    Tag: tree, design ds (design data structure)

    A quadtree is a tree data in which each internal node has exactly 
    four children: topLeft, topRight, bottomLeft and bottomRight. Quad 
    trees are often used to partition a two-dimensional space by recursively 
    subdividing it into four quadrants or regions.

    We want to store True/False information in our quad tree. The quad tree 
    is used to represent a N * N boolean grid. For each node, it will be 
    subdivided into four children nodes until the values in the region it 
    represents are all the same. 
    Each node has another two boolean attributes : isLeaf and val. 
    isLeaf is true if and only if the node is a leaf node. 
    The val attribute for a leaf node contains the value of the region it represents.

    For example, below are two quad trees A and B:
    A:
    +-------+-------+              topLeft: T
    |       |       |              topRight: T
    |   T   |   T   |              bottomLeft: F
    |       |       |              bottomRight: F
    +-------+-------+
    |       |       |
    |   F   |   F   |
    |       |       |
    +-------+-------+
    
    B:               
    +-------+---+---+                 topLeft: T
    |       | F | F |                 topRight:
    |   T   +---+---+                     topLeft: F
    |       | T | T |                     topRight: F
    +-------+---+---+                     bottomLeft: T
    |       |       |                     bottomRight: T
    |   T   |   F   |                 bottomLeft: T
    |       |       |                 bottomRight: F
    +-------+-------+

    Your task is to implement a function that will take two quadtrees 
    and return a quadtree that represents the logical OR (or union) of the two trees.

    A:                 B:                 C (A or B):
    +-------+-------+  +-------+---+---+  +-------+-------+
    |       |       |  |       | F | F |  |       |       |
    |   T   |   T   |  |   T   +---+---+  |   T   |   T   |
    |       |       |  |       | T | T |  |       |       |
    +-------+-------+  +-------+---+---+  +-------+-------+
    |       |       |  |       |       |  |       |       |
    |   F   |   F   |  |   T   |   F   |  |   T   |   F   |
    |       |       |  |       |       |  |       |       |
    +-------+-------+  +-------+-------+  +-------+-------+

    Note:
    -  Both A and B represent grids of size N * N.
    -  N is guaranteed to be a power of 2.
    -  If you want to know more about the quad tree, you can refer to its wiki.
    -  The logic OR operation is defined as this: "A or B" is true if A is true, 
        or if B is true, or if both A and B are true.
"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, A: 'Node', B: 'Node') -> 'Node':
        # return the union value if either is a leaf node
        if A.isLeaf:
            return A.val and A or B
        elif B.isLeaf:
            return B.val and B or A
        else:
            TL = self.intersect(A.topLeft, B.topLeft)
            TR = self.intersect(A.topRight, B.topRight)
            BL = self.intersect(A.bottomLeft, B.bottomLeft)
            BR = self.intersect(A.bottomRight, B.bottomRight)
            # if all the quadrants are same make it a Leaf node
            if TL.isLeaf and TR.isLeaf and BL.isLeaf and BR.isLeaf and TL.val == TR.val == BL.val == BR.val:
                C = Node(TL.val, True, None, None, None, None)
            else:
                C = Node(False, False, TL, TR, BL, BR)
        return C


T, F = True, False
yes, no = True, False
N = None
A = Node(None, no, topLeft=Node(T, yes, N, N, N, N), topRight=Node(T, yes, N, N, N, N),
         bottomLeft=Node(F, yes, N, N, N, N), bottomRight=Node(F, yes, N, N, N, N))

B_TopRight = Node(None, no, topLeft=Node(F, yes, N, N, N, N), topRight=Node(F, yes, N, N, N, N),
                  bottomLeft=Node(T, yes, N, N, N, N), bottomRight=Node(T, yes, N, N, N, N))
B = Node(None, no, topLeft=Node(T, yes, N, N, N, N), topRight=B_TopRight,
         bottomLeft=Node(T, yes, N, N, N, N), bottomRight=Node(F, yes, N, N, N, N))
Solution().intersect(A, B)
print("Tests Passed!!")
