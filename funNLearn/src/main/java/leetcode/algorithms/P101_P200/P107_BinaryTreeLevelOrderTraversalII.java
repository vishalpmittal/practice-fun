/*
* Tag: tree
*
* Given a binary tree, return the bottom-up level order traversal of 
* its nodes' values. (ie, from left to right, level by level from leaf to root).
* 
* For example:
* Given binary tree {3,9,20,#,#,15,7},
*     3
*    / \
*   9  20
*     /  \
*    15   7
* 
* return its bottom-up level order traversal as:
* [
*   [15,7],
*   [9,20],
*   [3]
* ]
*/

package leetcode.algorithms.P101_P200;

import java.util.ArrayList;
import java.util.List;

import leetcode.dependencies.TreeNode;

public class P107_BinaryTreeLevelOrderTraversalII {

	public static List<List<Integer>> levelOrderBottom(TreeNode root) {
		List<TreeNode> list = new ArrayList<TreeNode>();
		List<List<Integer>> listOfList = new ArrayList<List<Integer>>();
		
		if(root == null)
			return listOfList;
		
		list.add(root);
		levelOrderHelper(list, listOfList);
		return listOfList;
	}

	public static void levelOrderHelper(List<TreeNode> list, List<List<Integer>> listOfList) {
		if (list.isEmpty())
			return;

		List<TreeNode> subList = new ArrayList<TreeNode>();
		List<Integer> intList = new ArrayList<Integer>();

		for (TreeNode tn : list) {
			intList.add(tn.val);
			if (tn.left != null)
				subList.add(tn.left);
			if (tn.right != null)
				subList.add(tn.right);
		}

		levelOrderHelper(subList, listOfList);
		listOfList.add(intList);
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

		System.out.println(TreeNode.printTree(tn1));
		
		// Answer should be this:
		// [[14], [8, 9, 10, 11, 12, 13], [4, 5, 6, 7], [2, 3], [1]]
		System.out.println(levelOrderBottom(tn1));
	}
}
