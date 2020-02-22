package dsAlgo.leetcode.dependencies;

import java.util.HashMap;

public class TreeNode {
	public int val;
	public TreeNode left;
	public TreeNode right;

	public TreeNode(int x) {
		val = x;
	}

	public int getVal() {
		return val;
	}

	public void setVal(int val) {
		this.val = val;
	}

	public TreeNode getLeft() {
		return left;
	}

	public void setLeft(TreeNode left) {
		this.left = left;
	}

	public TreeNode getRight() {
		return right;
	}

	public void setRight(TreeNode right) {
		this.right = right;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder(this.val + ": [");
		if (this.left != null)
			sb.append("left=" + left.val);

		if (this.right != null)
			sb.append(", right=" + right.val);

		return sb.toString() + "]";
	}

	public static String printTree(TreeNode tn) {
		if (tn == null)
			return "";
		else {
			StringBuilder sb = new StringBuilder(tn.toString());
			String str = printTree(tn.left);
			if (str.compareTo("") != 0)
				sb.append("\n" + str);

			str = printTree(tn.right);
			if (str.compareTo("") != 0)
				sb.append("\n" + str);

			return sb.toString();
		}
	}

	// [1,2,3,5]
	// [[1,2], [3], [], []]
	public static TreeNode makeMeATree(int[] nodes, int[][] connLoc) {
		if (nodes == null || nodes.length == 0)
			return null;

		HashMap<Integer, TreeNode> map = new HashMap<Integer, TreeNode>();
		TreeNode rn = new TreeNode(nodes[0]);
		map.put(0, rn);

		for (int i = 0; i < nodes.length; i++) {
			map.putIfAbsent(i, new TreeNode(nodes[i]));

			try {
				int left = connLoc[i][0];
				if (left >= 0) {
					map.putIfAbsent(left, new TreeNode(nodes[left]));
					map.get(i).left = map.get(left);
				}
			} catch (ArrayIndexOutOfBoundsException aiobe) {
			}
			try {
				int right = connLoc[i][1];
				if (right >= 0) {
					map.putIfAbsent(right, new TreeNode(nodes[right]));
					map.get(i).right = map.get(right);
				}
			} catch (ArrayIndexOutOfBoundsException aiobe) {
			}

		}
		return rn;
	}
}
