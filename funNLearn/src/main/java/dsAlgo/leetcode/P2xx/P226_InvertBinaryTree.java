/**
 * Tag: tree
 *
 * Invert a binary tree or create a mirror reflection of the binary tree
 * 
 *      4
 *    /   \
 *   2     7
 *  / \   / \
 * 1   3 6   9
 * to
 *      4
 *    /   \
 *   7     2
 *  / \   / \
 * 9   6 3   1
*/

package dsAlgo.leetcode.P2xx;

import dsAlgo.leetcode.dependencies.TreeNode;

public class P226_InvertBinaryTree {
	public static TreeNode invertTree(TreeNode root) {
		if (root != null) {
			TreeNode tmpNode = root.left;
			root.left = root.right;
			root.right = tmpNode;

			invertTree(root.left);
			invertTree(root.right);
		}
		return root;
	}

	public static TreeNode invertTree_2(TreeNode root) {
		if (root != null) {
			TreeNode tmpRight = root.right;
			root.right = invertTree_2(root.left);
			root.left = invertTree_2(tmpRight);
		}
		return root;
	}

	public static void main(String[] args) {
		//|
		//|                   1
		//|               /       \
		//|          2                  3
		//|        /   \              /   \
		//|     4        5         6         7
		//|    /  \       \      /  \       /
		//|  8     9      10   11    12    13
		//|   \              
		//|   14
		//

		TreeNode tn1 = new TreeNode(1);
		TreeNode tn2 = new TreeNode(2);
		TreeNode tn3 = new TreeNode(3);
		TreeNode tn4 = new TreeNode(4);
		TreeNode tn5 = new TreeNode(5);
		TreeNode tn6 = new TreeNode(6);
		TreeNode tn7 = new TreeNode(7);
		TreeNode tn8 = new TreeNode(8);
		TreeNode tn9 = new TreeNode(9);
		TreeNode tn10 = new TreeNode(10);
		TreeNode tn11 = new TreeNode(11);
		TreeNode tn12 = new TreeNode(12);
		TreeNode tn13 = new TreeNode(13);
		TreeNode tn14 = new TreeNode(14);

		tn1.setLeft(tn2);
		tn1.setRight(tn3);
		tn2.setLeft(tn4);
		tn2.setRight(tn5);
		tn3.setLeft(tn6);
		tn3.setRight(tn7);
		tn4.setLeft(tn8);
		tn4.setRight(tn9);
		tn5.setRight(tn10);
		tn6.setLeft(tn11);
		tn6.setRight(tn12);
		tn7.setLeft(tn13);
		tn8.setRight(tn14);

		//		System.out.println(TreeNode.printTree(tn1));
		invertTree_2(tn1);
		System.out.println(TreeNode.printTree(tn1));
	}

}
