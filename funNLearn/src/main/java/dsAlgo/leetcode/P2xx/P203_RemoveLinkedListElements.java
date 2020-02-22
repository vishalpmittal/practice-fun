/**
 * Tag: linked list
 *
 * Remove all elements from a linked list of integers that have value val.
 * 
 * Example
 * Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
 * Return: 1 --> 2 --> 3 --> 4 --> 5
 * 
 */

package dsAlgo.leetcode.P2xx;

import dsAlgo.leetcode.dependencies.ListNode;

public class P203_RemoveLinkedListElements {

	public static ListNode removeElements(ListNode head, int val) {
		if (head == null)
			return null;

		while (head != null && head.val == val)
			head = head.next;

		ListNode curr = head;
		while (curr != null && curr.next != null) {
			if (curr.next.val == val)
				curr.next = curr.next.next;
			else
				curr = curr.next;
		}
		return head;
	}

	public static void main(String[] args) {
		/*
		 * [R -> 2 -> 3 -> 4 -> 5 -> 6 -> 7]
		 * [R -> 1 -> 2 -> 3 -> 4 -> 5 -> 6]
		 * [R -> 1 -> 2 -> 3 -> 5 -> 6 -> 7]
		 * [R]
		 * [R -> 2 -> 3 -> 4 -> 5]
		 */
		System.out.println(ListNode.getListString(
			removeElements(ListNode.makeMeAList(new int[] { 1, 2, 3, 4, 5, 6, 7 }), 1)
			));
		System.out.println(ListNode.getListString(
			removeElements(ListNode.makeMeAList(new int[] { 1, 2, 3, 4, 5, 6, 7 }), 7)
			));
		System.out.println(ListNode.getListString(
			removeElements(ListNode.makeMeAList(new int[] { 1, 2, 3, 4, 5, 6, 7 }), 4)
			));
		System.out.println(ListNode.getListString(
			removeElements(ListNode.makeMeAList(new int[] { 1, 1 }), 1)
			));
		System.out.println(ListNode.getListString(
			removeElements(ListNode.makeMeAList(new int[] { 1, 1, 2, 3, 4, 5 }), 1)
			));
	}
}
