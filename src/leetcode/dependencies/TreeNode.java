package leetcode.dependencies;

public class TreeNode {
	int val;
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
}
