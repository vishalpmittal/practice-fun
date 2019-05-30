/*
 * Given a binary tree, find its minimum depth.
 * The minimum depth is the number of nodes along the shortest 
 * path from the root node down to the nearest leaf node.
 * 
 */

package leetcode.algorithms.P101_P200;

import leetcode.dependencies.TreeNode;

public class P111_MinimumDepthOfBinaryTree {

	public static int minDepth(TreeNode root) {
		if (root == null)
			return 0;
		int left = minDepth(root.left);
		int right = minDepth(root.right);
		return (left == 0 || right == 0) ? left + right + 1 : Math.min(left, right) + 1;
	}

	public static void main(String[] args) {
		//|
		//|                   1
		//|               /       \
		//|          2                  3
		//|        /   \              /   \
		//|     4        5         6         7
		//|    /  \       \      /  \       
		//|  8     9      10   11    12    
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
		tn8.setRight(tn14);

		System.out.println(TreeNode.printTree(tn1));
		System.out.println(minDepth(tn1));

	}
}
