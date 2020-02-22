/**
 * Tag: tree
 * 
 * Given a non-empty binary search tree and a target value, 
 * find the value in the BST that is closest to the target.
 * 
 * Note:
 * -  Given target value is a floating point.
 * -  You are guaranteed to have only one unique value in the BST that 
 * is closest to the target.
 *
 * Example:
 * Input: root = [4,2,5,1,3], target = 3.714286
 *     4
 *    / \
 *   2   5
 *  / \
 * 1   3
 * Output: 4
 */

package dsAlgo.leetcode.P2xx;

import dsAlgo.leetcode.dependencies.TreeNode;

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
		// System.out.println("All Tests passed");
	}
}
