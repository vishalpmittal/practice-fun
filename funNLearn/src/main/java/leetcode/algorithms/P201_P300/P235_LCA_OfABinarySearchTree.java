/**
 * Tag: tree
 *
 * Given a binary search tree (BST), find the lowest common 
 * ancestor (LCA) of two given nodes in the BST.
 * 
 * According to the definition of LCA on Wikipedia: 
 * “The lowest common ancestor is defined between two nodes v and w as the 
 * lowest node in T that has both v and w as descendants (where we allow a node 
 * to be a descendant of itself).”
 *
 *        _______6______
 *       /              \
 *    ___2__          ___8__
 *   /      \        /      \
 *   0      _4       7       9
 *         /  \
 *         3   5
 * 
 * For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. 
 * Another example is LCA of nodes 2 and 4 is 2, since a node can be a 
 * descendant of itself according to the LCA definition.
 */

package leetcode.algorithms.P201_P300;

import leetcode.dependencies.TreeNode;

public class P235_LCA_OfABinarySearchTree {

	public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
		if ((root.val - p.val) * (root.val - q.val) < 1) {
			return root;
		} else {
			if (root.val > p.val) {
				return lowestCommonAncestor(root.left, p, q);
			} else {
				return lowestCommonAncestor(root.right, p, q);
			}
		}
	}

	// same solution as above but single liner
	public TreeNode lowestCommonAncestor_1(TreeNode root, TreeNode p, TreeNode q) {
		return ((root.val - p.val) * (root.val - q.val) < 1) ? root
				: (root.val > p.val ? lowestCommonAncestor_1(root.left, p, q)
						: lowestCommonAncestor_1(root.right, p, q));
	}

	public static void main(String[] args) {
		TreeNode tn0 = new TreeNode(0);
		TreeNode tn2 = new TreeNode(2);
		TreeNode tn4 = new TreeNode(4);
		TreeNode tn3 = new TreeNode(3);
		TreeNode tn5 = new TreeNode(5);
		TreeNode tn6 = new TreeNode(6);
		TreeNode tn7 = new TreeNode(7);
		TreeNode tn8 = new TreeNode(8);
		TreeNode tn9 = new TreeNode(9);

		tn6.left = tn2;
		tn6.right = tn8;
		tn2.left = tn0;
		tn2.right = tn4;
		tn4.left = tn3;
		tn4.right = tn5;

		tn8.left = tn7;
		tn8.right = tn9;

		System.out.println(TreeNode.printTree(tn6));
	}
}
