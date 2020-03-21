/**
 * tag: BST, tree
 */

package dsAlgo.tree;

class BTreeNode<T> {
    public int value;
    public BTreeNode left;
    public BTreeNode right;

    public BTreeNode(int value) {
        this.value = value;
    }
}

class BST {
    public BTreeNode root;

    public BST insert(int value) {
        BTreeNode node = new BTreeNode<>(value);
        if (root == null) {
            root = node;
            return this;
        }
        insertRec(root, node);
        return this;
    }

    private void insertRec(BTreeNode latestRoot, BTreeNode node) {

        if (latestRoot.value > node.value) {

            if (latestRoot.left == null) {
                latestRoot.left = node;
                return;
            } else {
                insertRec(latestRoot.left, node);
            }
        } else {
            if (latestRoot.right == null) {
                latestRoot.right = node;
                return;
            } else {
                insertRec(latestRoot.right, node);
            }
        }
    }

    public int findMinimum() {
        if (root == null) {
            return 0;
        }
        BTreeNode currNode = root;
        while (currNode.left != null) {
            currNode = currNode.left;
        }
        return currNode.value;
    }

    public int findMaximum() {
        if (root == null) {
            return 0;
        }

        BTreeNode currNode = root;
        while (currNode.right != null) {
            currNode = currNode.right;
        }
        return currNode.value;
    }

    public void printInorder() {
        printInOrderRec(root);
        System.out.println("");
    }

    private void printInOrderRec(BTreeNode currRoot) {
        if (currRoot == null) {
            return;
        }
        printInOrderRec(currRoot.left);
        System.out.print(currRoot.value + ", ");
        printInOrderRec(currRoot.right);
    }

    public void printPreorder() {
        printPreOrderRec(root);
        System.out.println("");
    }

    private void printPreOrderRec(BTreeNode currRoot) {
        if (currRoot == null) {
            return;
        }
        System.out.print(currRoot.value + ", ");
        printPreOrderRec(currRoot.left);
        printPreOrderRec(currRoot.right);
    }

    public void printPostorder() {
        printPostOrderRec(root);
        System.out.println("");
    }

    private void printPostOrderRec(BTreeNode currRoot) {
        if (currRoot == null) {
            return;
        }
        printPostOrderRec(currRoot.left);
        printPostOrderRec(currRoot.right);
        System.out.print(currRoot.value + ", ");
    }
}

class BinarySearchTreeSample {
    public static void main(String[] args) {
        BST bst = new BST();
        bst.insert(40).insert(25).insert(78).insert(10).insert(3).insert(17).insert(32).insert(30).insert(38).insert(78)
                .insert(50).insert(93);
        System.out.println("Inorder traversal");
        bst.printInorder();

        System.out.println("Preorder Traversal");
        bst.printPreorder();

        System.out.println("Postorder Traversal");
        bst.printPostorder();

        System.out.println("The minimum value in the BST: " + bst.findMinimum());
        System.out.println("The maximum value in the BST: " + bst.findMaximum());

    }
}