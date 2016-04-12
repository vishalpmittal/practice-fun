/*
 * Given a binary tree, find its maximum depth.
 * 
 * The maximum depth is the number of nodes along the longest path from 
 * the root node down to the farthest leaf node.
 */

package leetcode;

// Definition for a binary tree node.
class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
}

public class P104_MaximumDepthOfBinaryTree {
	public static int maxDepth(TreeNode root) {
		return root==null? 0 : Math.max(maxDepth(root.left), maxDepth(root.right))+1;
	}

	public static void main(String[] args) {
		TreeNode tn1 = new TreeNode(4);
		TreeNode tn2 = new TreeNode(4);
		TreeNode tn3 = new TreeNode(4);
		TreeNode tn4 = new TreeNode(4);
		TreeNode tn5 = new TreeNode(4);
		TreeNode tn6 = new TreeNode(4);
		TreeNode tn7 = new TreeNode(4);
		TreeNode tn8 = new TreeNode(4);
		TreeNode tn9 = new TreeNode(4);
		TreeNode tn10 = new TreeNode(4);
		TreeNode tn11 = new TreeNode(4);
		TreeNode tn12 = new TreeNode(4);		
		TreeNode tn13 = new TreeNode(4);		
		
		tn1.left = tn2;
		tn1.right = tn3;
		
		tn2.left = tn4;
		tn2.right = tn5;
		
		tn3.left = tn6;
		tn3.right = tn7;
		
		tn4.left = tn8;
		tn4.right = tn9;
		
		tn5.left = tn10;
		tn5.left = tn11;

		tn6.left = tn12;
		tn6.right = tn13;
		
		System.out.println(maxDepth(tn1));
	}
}
