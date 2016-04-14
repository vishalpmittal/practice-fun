package leetcode.dependencies;

public class ListNode {
	public int val;
	public ListNode next;

	public ListNode(int x) {
		val = x;
	}

	@Override
	public String toString() {
		return ""+ this.val;
	}
	
	public static String getListString(ListNode ln){
		StringBuilder sb = new StringBuilder("[R");
		ListNode cn = ln;
		while (cn != null){
			sb.append(" -> "+ cn.toString());
			cn = cn.next;
		}
		sb.append("]");
		return sb.toString();
	}
	
}
