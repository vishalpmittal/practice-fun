"""
    Tag: tree

    Top view of the above binary tree is 2 1 3 6
        1
      /   \
    2       3
      \   
        4  
          \
            5
             \
               6
"""


class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0


def topview(root):
    if root == None:
        return
    q = []
    m = dict()
    hd = 0   #horizontal distance
    root.hd = hd

    q.append(root)
    while len(q):
        root = q[0]
        hd = root.hd

        if hd not in m:
            m[hd] = root.data
        if root.left:
            root.left.hd = hd - 1
            q.append(root.left)

        if root.right:
            root.right.hd = hd + 1
            q.append(root.right)

        q.pop(0)
    for i in sorted(m):
        print(m[i], end="")


if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.right = newNode(4)
    root.left.right.right = newNode(5)
    root.left.right.right.right = newNode(6)
    print("Following are nodes in top", "view of Binary Tree")
    topview(root)
