package leetcode.tree;
/*
* Given a binary tree, check whether it is a mirror of itself 
* (ie, symmetric around its center).
* 
* For example, this binary tree is symmetric:
*     1
*    / \
*   2   2
*  / \ / \
* 3  4 4  3
* 
* But the following is not:
*     1
*    / \
*   2   2
*    \   \
*    3    3
* 
* Note:
* Bonus points if you could solve it both recursively and iteratively.
* 
* OJ's Binary Tree Serialization:
* The serialization of a binary tree follows a level order traversal, 
* where '#' signifies a path terminator where no node exists below.
* 
* Here's an example:
*    1
*   / \
*  2   3
*     /
*    4
*     \
*      5
* The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
*/

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import leetcode.dependencies.TreeNode;

import static org.junit.Assert.assertTrue;

import java.util.Stack;

import static org.junit.Assert.assertFalse;

public class P101_SymmetricTree {

	//Recursive solution
	public static boolean isSymmetric_1(TreeNode left, TreeNode right) {
		if (left == null || right == null)
			return left == right;
		if (left.val != right.val)
			return false;
		return isSymmetric_1(left.left, right.right) && isSymmetric_1(left.right, right.left);
	}

	public static boolean isSymmetric_1(TreeNode root) {
		return root == null || isSymmetric_1(root.left, root.right);
	}

	//Iterative solution
	public static boolean isSymmetric_2(TreeNode root) {
		if (root == null)
			return true;

		Stack<TreeNode> stack = new Stack<TreeNode>();
		TreeNode left, right;
		if (!process(root.left, root.right, stack))
			return false;

		while (!stack.empty()) {
			if (stack.size() % 2 != 0)
				return false;
			right = stack.pop();
			left = stack.pop();
			if (right.val != left.val)
				return false;
			if (!process(left.left, right.right, stack))
				return false;
			if (!process(left.right, right.left, stack))
				return false;
		}
		return true;
	}

	public static boolean process(TreeNode a, TreeNode b, Stack<TreeNode> s) {
		if (a != null) {
			if (b == null)
				return false;
			s.push(a);
			s.push(b);
		} else if (b != null)
			return false;
		return true;
	}

	public static boolean isSymmetric(TreeNode root) {
		return isSymmetric_2(root);
	}

	@Test
	public void test() {
		TreeNode tn1 = new TreeNode(1);
		TreeNode tn2 = new TreeNode(2);
		TreeNode tn2_ = new TreeNode(2);
		TreeNode tn3 = new TreeNode(3);
		TreeNode tn3_ = new TreeNode(3);
		TreeNode tn4 = new TreeNode(4);
		TreeNode tn4_ = new TreeNode(4);
		
		tn1.left = tn2;
		tn1.right = tn2_;
		tn2.left = tn3;
		tn2.right = tn4;
		tn2_.left = tn4_;
		tn2_.right = tn3_;
		
		System.out.println(TreeNode.printTree(tn1));
		assertTrue("Test1", isSymmetric(tn1));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P101_SymmetricTree.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
