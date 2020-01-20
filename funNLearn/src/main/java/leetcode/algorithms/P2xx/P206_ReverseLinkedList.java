/**
 * Tag: linked list
 *
 * Reverse a singly linked list
 */

package leetcode.algorithms.P2xx;

import leetcode.dependencies.ListNode;

public class P206_ReverseLinkedList {

	public static ListNode reverseList(ListNode head) {
		if (head == null || head.next == null)
			return head;

		ListNode c1 = head;
		ListNode c2 = c1.next;
		ListNode c3 = c2.next;
		c1.next = null;

		while (c2 != null) {
			c2.next = c1;
			c1 = c2;
			c2 = c3;
			c3 = (c3 == null) ? null : c3.next;
		}
		return c1;
	}

	public static ListNode reverseList_1(ListNode head) {
		/* recursive solution */
		return reverseListInt(head, null);
	}

	private static ListNode reverseListInt(ListNode head, ListNode newHead) {
		if (head == null)
			return newHead;
		ListNode next = head.next;
		head.next = newHead;
		return reverseListInt(next, head);
	}

	public static void main(String[] args) {
		ListNode ln1 = new ListNode(1);
		ListNode ln2 = new ListNode(2);
		ListNode ln3 = new ListNode(3);
		ListNode ln4 = new ListNode(4);
		ListNode ln5 = new ListNode(5);

		ln1.next = ln2;
		ln2.next = ln3;
		ln3.next = ln4;
		ln4.next = ln5;

		System.out.println(ListNode.getListString(ln1));
		System.out.println(ListNode.getListString(reverseList_1(ln1)));

	}

}
