/*
* Given a binary tree, return all root-to-leaf paths.
* For example, given the following binary tree:
* 
*    1
*  /   \
* 2     3
*  \
*   5
* All root-to-leaf paths are:
* 
* ["1->2->5", "1->3"]
*/

package leetcode.tree;

import java.util.ArrayList;
import java.util.List;
import leetcode.dependencies.TreeNode;

public class P257_BinaryTreePaths {

	public static List<String> binaryTreePaths(TreeNode root) {
		List<String> pathList = new ArrayList<String>();
		if (root == null)
			return pathList;

		binaryTreePaths(root, "", pathList);
		return pathList;
	}

	public static void binaryTreePaths(TreeNode node, String currPath, List<String> pathList) {
		currPath = currPath + node.val;
		if (node.left == null && node.right == null) {
			pathList.add(currPath);
			return;
		}

		if (node.left != null)
			binaryTreePaths(node.left, currPath + "->", pathList);

		if (node.right != null)
			binaryTreePaths(node.right, currPath + "->", pathList);
	}

	public static void main(String[] args) {
		int[] nodes = new int[] { 1, 2, 3, 5 };
		int[][] locations = new int[][] { new int[] { 1, 2 }, new int[] { -1, 3 } };

		TreeNode rn = TreeNode.makeMeATree(nodes, locations);
		System.out.println(TreeNode.printTree(rn));
		// [1->2->5, 1->3]
		System.out.println(binaryTreePaths(rn));

	}
}
