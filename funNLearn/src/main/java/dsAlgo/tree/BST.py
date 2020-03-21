"""
    Tag: tree, BST
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

    def insert_value(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert_value(root.left, key)
        else:
            root.right = self.insert_value(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

    def minValueNode(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def countNodes(self, root):
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def sortedArrayToBST(self, arr, root):
        if root is None:
            return

        # First update the left subtree
        self.arrayToBST(arr, root.left)

        # now update root's data delete the value from array
        root.data = arr[0]
        arr.pop(0)

        # Finally update the right subtree
        self.arrayToBST(arr, root.right)

    def binaryTreeToBST(self, root):
        if root is None:
            return

        # Create the temp array and store the inorder traveral of tree
        arr = []
        self.storeInorder(root, arr)
        arr.sort()

        # copy array elements back to BST
        self.arrayToBST(arr, root)

    def storeinorderInSet(self, root, s):
        if not root:
            return

        self.storeinorderInSet(root.left, s)
        s.add(root.data)
        self.storeinorderInSet(root.right, s)

    def setToBST(self, s, root):
        if not root:
            return

        self.setToBST(s, root.left)

        # iterator initially pointing to the beginning of set
        it = next(iter(s))
        # copying the item at beginning of  set(sorted) to the tree.
        root.data = it
        # now erasing the beginning item from set.
        s.remove(it)

        # now move to right subtree  and update items
        self.setToBST(s, root.right)

    def binaryTreeToBST(self, root):
        """
            this one creates BST while traversing in order 
            thus it keeps the original form of the binary tree
        """
        s = set()

        # populating the set with the tree's  inorder traversal data
        storeinorderInSet(root, s)

        # now sets are by default sorted as they are implemented using self-balancing BST
        # copying items from set to the tree  while inorder traversal which makes a BST
        setToBST(s, root)

    def deleteNode(self, root, key):
        # Base Case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key then it lies in left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If the kye to be delete is greater than the root's key then it lies in right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.val = temp.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)

        return root


def test_bst():
    bst = BST()
    root = None
    root = bst.insert_value(root, 50)
    root = bst.insert_value(root, 30)
    root = bst.insert_value(root, 20)
    root = bst.insert_value(root, 40)
    root = bst.insert_value(root, 70)
    root = bst.insert_value(root, 60)
    root = bst.insert_value(root, 80)

    print("Inorder traversal of the given tree")
    bst.inorder(root)

    print("\nDelete 20")
    root = bst.deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    bst.inorder(root)

    print("\nDelete 30")
    root = bst.deleteNode(root, 30)
    print("Inorder traversal of the modified tree")
    bst.inorder(root)

    print("\nDelete 50")
    root = bst.deleteNode(root, 50)
    print("Inorder traversal of the modified tree")
    bst.inorder(root)


test_bst()
