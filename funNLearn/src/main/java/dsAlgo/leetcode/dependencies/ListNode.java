package dsAlgo.leetcode.dependencies;

public class ListNode {
	public int val;
	public ListNode next;

	public ListNode(int x) {
		val = x;
	}

	@Override
	public String toString() {
		return "" + this.val;
	}

	public static String getListString(ListNode ln) {
		StringBuilder sb = new StringBuilder("[R");
		ListNode cn = ln;
		while (cn != null) {
			sb.append(" -> " + cn.toString());
			cn = cn.next;
		}
		sb.append("]");
		return sb.toString();
	}

	public static ListNode makeMeAList(int[] values) {
		if (values == null || values.length == 0)
			return null;

		ListNode head = new ListNode(values[0]);
		ListNode curr = head;
		for (int i = 1; i < values.length; i++) {
			curr.next = new ListNode(values[i]);
			curr = curr.next;
		}
		return head;
	}
}
