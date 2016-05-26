/*
 * Given a linked list, swap every two adjacent nodes and return its head.
 * 
 * For example,
 * Given 1->2->3->4, you should return the list as 2->1->4->3.
 * 
 * Your algorithm should use only constant space. 
 * You may not modify the values in the list, only nodes itself can be changed.
 */

package leetcode.lists;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import leetcode.dependencies.ListNode;

public class P024_SwapNodesInPairs {
	// Recursive solution
	public static ListNode swapPairs_1(ListNode head) {
		if (head == null || head.next == null)
			return head;

		ListNode t1 = head;
		head = head.next;
		ListNode t2 = head.next;
		head.next = t1;
		t1.next = swapPairs_1(t2);
		return head;
	}

	// Iterative solution
	public static ListNode swapPairs_2(ListNode head) {
		ListNode dummy = new ListNode(0);
		dummy.next = head;
		ListNode current = dummy;
		while (current.next != null && current.next.next != null) {
			ListNode first = current.next;
			ListNode second = current.next.next;
			first.next = second.next;
			current.next = second;
			current.next.next = first;
			current = current.next.next;
		}
		return dummy.next;
	}

	public static ListNode swapPairs(ListNode head) {
		return swapPairs_1(head);
	}

	@Test
	public void test() {
		ListNode l1n1 = new ListNode(1);
		ListNode l1n2 = new ListNode(2);
		ListNode l1n3 = new ListNode(3);
		ListNode l1n4 = new ListNode(4);

		l1n1.next = l1n2;
		l1n2.next = l1n3;
		l1n3.next = l1n4;

		//System.out.println(ListNode.getListString(swapPairs(l1n1)));
		assertTrue("Test1", ListNode.getListString(swapPairs(l1n1)).compareTo("[R -> 2 -> 1 -> 4 -> 3]") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P024_SwapNodesInPairs.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
