/**
 * Tag: linked list, sort
 * 
 * Given a sorted linked list, delete all duplicates such that 
 * each element appear only once.
 * 
 * For example,
 * Given 1->1->2, return 1->2.
 * Given 1->1->2->3->3, return 1->2->3.
 */
package leetcode.algorithms.P001_P100;

import leetcode.dependencies.ListNode;

public class P083_RemoveDuplicatesFromSortedList {

	public static ListNode deleteDuplicates(ListNode head) {
		ListNode cn = head;
		while (cn != null && cn.next != null) {
			if (cn.val == cn.next.val) {
				ListNode temp = cn.next;
				cn.next = cn.next.next;
				temp.next = null;
			} else
				cn = cn.next;
		}
		return head;
	}

	public static ListNode deleteDuplicates_rec(ListNode head) {
		if (head == null || head.next == null)
			return head;
		head.next = deleteDuplicates_rec(head.next);
		return head.val == head.next.val ? head.next : head;
	}

	public static void main(String[] args) {
		ListNode ln1 = new ListNode(1);
		ListNode ln2 = new ListNode(1);
		ListNode ln3 = new ListNode(2);
		ListNode ln4 = new ListNode(3);
		ListNode ln5 = new ListNode(3);

		ln1.next = ln2;
		ln2.next = ln3;
		ln3.next = ln4;
		ln4.next = ln5;

		System.out.println(ListNode.getListString(ln1));
		System.out.println(ListNode.getListString(deleteDuplicates(ln1)));

	}
}
