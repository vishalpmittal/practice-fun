/**
 * Tag: linked list
 * 
 * Given a linked list, remove the nth node from the end of list and return its head.
 * 
 * For example,
 * Given linked list: 1->2->3->4->5, and n = 2.
 * 
 * After removing the second node from the end, the linked list becomes 1->2->3->5.
 * 
 * Note:
 * Given n will always be valid.
 * Try to do this in one pass.
 */

package leetcode.algorithms.P0xx;

import leetcode.dependencies.ListNode;

public class P019_RemoveNthNodeFromEndOfList {
	public static ListNode removeNthFromEnd(ListNode head, int n) {
		ListNode leader = head;
		ListNode follower = head;

		for (int i = 0; i < n; i++) {
			leader = leader.next;
		}

		if (leader == null)
			return head.next;

		while (leader.next != null) {
			leader = leader.next;
			follower = follower.next;
		}
		follower.next = follower.next.next;
		return head;
	}

	public static void main(String[] args) {
		ListNode ln1 = new ListNode(1);
		ListNode ln2 = new ListNode(2);
		ListNode ln3 = new ListNode(3);
		ListNode ln4 = new ListNode(4);
		ListNode ln5 = new ListNode(5);
		ListNode ln6 = new ListNode(6);
		ListNode ln7 = new ListNode(7);

		ln1.next = ln2;
		ln2.next = ln3;
		ln3.next = ln4;
		ln4.next = ln5;
		ln5.next = ln6;
		ln6.next = ln7;

		/*
		 * [R -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7]
		 * [R -> 2 -> 3 -> 4 -> 5 -> 6 -> 7]
		 * [R -> 2 -> 3 -> 4 -> 6 -> 7]
		 */
		System.out.println(ListNode.getListString(ln1));
		System.out.println(ListNode.getListString(removeNthFromEnd(ln1, 7)));
		System.out.println(ListNode.getListString(removeNthFromEnd(ln2, 3)));

	}
}
