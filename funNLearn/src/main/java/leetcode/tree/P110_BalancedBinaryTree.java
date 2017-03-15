/*
 * Given a binary tree, determine if it is height-balanced.
 * For this problem, a height-balanced binary tree is defined as a binary 
 * tree in which the depth of the two subtrees of every node never differ by more than 1.
 */

package leetcode.tree;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import leetcode.dependencies.TreeNode;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P110_BalancedBinaryTree {

	public static int depth(TreeNode root) {
		if (root == null)
			return 0;
		return Math.max(depth(root.left), depth(root.right)) + 1;
	}

	/*
	 * Recursive method, O( N logN) solution.
	 * as we find out depth of each node separately and we compare them
	 * also we do this whole process for every node
	 */
	public static boolean isBalanced_1(TreeNode root) {
		if (root == null)
			return true;
		int left = depth(root.left);
		int right = depth(root.right);

		return Math.abs(left - right) <= 1 && isBalanced_1(root.left) && isBalanced_1(root.right);
	}

	/*
	 * O(N) Bottoms up solution
	 * Start at the bottom, Every iteration returns the height of the node
	 * but returns -1 if the height of its left/right subtrees differ by more than one.
	 *  
	 */
	public static int height(TreeNode root) {
		// bottom most, leaf node's left and right are null
		if (root == null)
			return 0;

		// if left side of tree is disbalanced return -1
		int left_height = height(root.left);
		if (left_height == -1)
			return -1;

		// if right side of tree is disbalanced return -1
		int right_height = height(root.right);
		if (right_height == -1)
			return -1;

		// if tree is disbalanced at this node.
		// as if left subtree's height is 3 and right's is 1
		if (Math.abs(left_height - right_height) > 1)
			return -1;

		// at this point the left_height and right_height are only 1 apart
		// so find the max and add 1 for this node and return
		return Math.max(left_height, right_height) + 1;
	}

	public static boolean isBalanced_2(TreeNode root) {
		int rootHeight = height(root);
		System.out.println("Root Height :" + rootHeight);
		return rootHeight != -1;
	}

	public static boolean isBalanced(TreeNode root) {
		return isBalanced_2(root);
	}

	@Test
	public void test() {
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

		assertTrue("Test1", isBalanced(tn1));

		tn2.right = null;
		assertFalse("Test2", isBalanced(tn1));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P110_BalancedBinaryTree.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
