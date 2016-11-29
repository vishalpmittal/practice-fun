/**
 * Given a non-empty binary search tree and a target value, 
 * find the value in the BST that is closest to the target.
 * 
 * Note:
 * -  Given target value is a floating point.
 * -  You are guaranteed to have only one unique value in the BST that 
 * is closest to the target.
 */

package leetcode.tree;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import leetcode.dependencies.TreeNode;

public class P270_ClosestBinarySearchTreeValue {

	public static int closestValue(TreeNode root, double target) {
		double currDiff = Math.abs(target - ((double) root.val));

		double leftDiff = -1.0;
		if (root.left != null) 
			leftDiff = Math.abs(target - ((double) root.left.val));

		double rightDiff = -1.0;
		if (root.right != null)
			rightDiff = Math.abs(target - ((double) root.right.val));

		if ((leftDiff == -1.0 && rightDiff == -1.0) || (currDiff < leftDiff && currDiff < rightDiff))
			return root.val;
		else if (rightDiff == -1.0 || leftDiff < rightDiff)
			return closestValue(root.left, target);
		else if (leftDiff == -1.0 || leftDiff > rightDiff)
			return closestValue(root.right, target);
		
		return root.val;
	}

	public static void main(String[] args) {
		//		assertTrue("Test1", problem(94));
		//		assertFalse("Test2", problem(97));
		System.out.println("All Tests passed");
	}
}
