/**
 * Tag: tree
 * 
 * Given a binary tree and a sum, determine if the tree has a root-to-leaf 
 * path such that adding up all the values along the path equals the given sum.
 * 
 * For example:
 * Given the below binary tree and sum = 22,
 *               5
 *              / \
 *             4   8
 *            /   / \
 *           11  13  4
 *          /  \      \
 *         7    2      1
 * return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
*/

package leetcode.algorithms.P1xx;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import leetcode.dependencies.TreeNode;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P112_PathSum {

	public static boolean hasPathSum(TreeNode root, int sum) {
		if (root == null)
			return false;
		if (root.left == null && root.right == null && root.val == sum)
			return true;

		return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
	}

	// A little more optimized code
	public static boolean hasPathSum_1(TreeNode root, int sum) {
		if (root == null)
			return false;
		if (root.left == null && root.right == null)
			return root.val == sum;

		return hasPathSum_1(root.left, sum - root.val) || hasPathSum_1(root.right, sum - root.val);
	}

	@Test
	public void test() {
		TreeNode tn5 = new TreeNode(5);
		TreeNode tn4 = new TreeNode(4);
		TreeNode tn8 = new TreeNode(8);
		TreeNode tn11 = new TreeNode(11);
		TreeNode tn13 = new TreeNode(13);
		TreeNode tn4_ = new TreeNode(4);
		TreeNode tn7 = new TreeNode(7);
		TreeNode tn2 = new TreeNode(2);
		TreeNode tn1 = new TreeNode(1);

		tn5.left = tn4;
		tn5.right = tn8;
		tn4.left = tn11;
		tn8.left = tn13;
		tn8.right = tn4_;

		tn11.left = tn7;
		tn11.right = tn2;
		tn4_.right = tn1;

		assertTrue("Test1", hasPathSum(tn5, 22));
		assertTrue("Test2", hasPathSum(tn11, 18));
		assertTrue("Test3", hasPathSum(tn7, 7));
		assertFalse("Test4", hasPathSum(null, 7));
		assertTrue("Test5", hasPathSum(tn8, 21));
		assertTrue("Test6", hasPathSum(tn8, 13));

	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P112_PathSum.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
