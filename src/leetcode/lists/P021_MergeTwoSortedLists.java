/*
 * Merge two sorted linked lists and return it as a new list. 
 * The new list should be made by splicing together the nodes of the first two lists.
 */

package leetcode.lists;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import leetcode.dependencies.ListNode;

public class P021_MergeTwoSortedLists {

	// Simple Iterative solution 
	public static ListNode mergeTwoLists_1(ListNode l1, ListNode l2) {
		if (l1 == null && l2 == null)
			return null;
		if (l1 == null)
			return l2;
		if (l2 == null)
			return l1;

		ListNode nroot = new ListNode(-1);
		ListNode nl = nroot;

		while (l1 != null && l2 != null) {
			if (l1.val < l2.val) {
				nl.next = l1;
				l1 = l1.next;
			} else {
				nl.next = l2;
				l2 = l2.next;
			}
			nl = nl.next;
		}

		if (l1 != null)
			nl.next = l1;

		if (l2 != null)
			nl.next = l2;

		return nroot.next;
	}

	// Recursive solution
	public static ListNode mergeTwoLists_2(ListNode l1, ListNode l2) {
		if (l1 == null)
			return l2;
		if (l2 == null)
			return l1;

		if (l1.val < l2.val) {
			l1.next = mergeTwoLists_2(l1.next, l2);
			return l1;
		} else {
			l2.next = mergeTwoLists_2(l2.next, l1);
			return l2;
		}
	}

	public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		return mergeTwoLists_2(l1, l2);
	}

	@Test
	public void test() {
		ListNode l1n1 = new ListNode(2);
		ListNode l1n2 = new ListNode(4);
		ListNode l1n3 = new ListNode(6);
		ListNode l1n4 = new ListNode(8);

		l1n1.next = l1n2;
		l1n2.next = l1n3;
		l1n3.next = l1n4;

		ListNode l2n1 = new ListNode(3);
		ListNode l2n2 = new ListNode(5);
		ListNode l2n3 = new ListNode(7);

		l2n1.next = l2n2;
		l2n2.next = l2n3;

		assertTrue("Test1", ListNode.getListString(mergeTwoLists(l1n1, l2n1))
				.compareTo("[R -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8]") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P021_MergeTwoSortedLists.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
