/*
 * Given two binary trees, write a function to check if they are equal or not.
 * 
 * Two binary trees are considered equal if they are structurally identical 
 * and the nodes have the same value.
 */

package leetcode;

import leetcode.dependencies.TreeNode;

public class P100_SameTree {

	public boolean isSameTree(TreeNode p, TreeNode q) {
		if (p == null || q == null)
			return p == q;
		else if (p.val == q.val)
			return true && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
		return false;
	}

	public static void main(String[] args) {

	}

}
