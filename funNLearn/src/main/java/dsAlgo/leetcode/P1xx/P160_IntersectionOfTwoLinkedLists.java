/**
 * Tag: linked list 
 *
 * Write a program to find the node at which the intersection of two singly linked lists begins.
 * 
 * For example, the following two linked lists:
 * A:          a1 → a2
 *                    ↘                     
 *                    c1 → c2 → c3
 *                    ↗            
 * B:     b1 → b2 → b3
 * 
 * begin to intersect at node c1.
 * 
 * Notes:
 * -  If the two linked lists have no intersection at all, return null.
 * -  The linked lists must retain their original structure after the function returns.
 * -  You may assume there are no cycles anywhere in the entire linked structure.
 * -  Your code should preferably run in O(n) time and use only O(1) memory.
 *
 * Take two pointers for List1 and List2. Now need to find out how to make them start
 * traversing so that equal length traversing is started.This can be done two ways:
 * 
 * Solution 1: 
 * -  Move list1/list2 pointer ahead until the length of both lists is same
 * 
 * Solution 2:
 * -  Iterate twice and swap the pointers at the end of first iteration. 
 * 	  This will make the pointers start at the same length point in the second iteration.
 */

package dsAlgo.leetcode.P1xx;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import dsAlgo.leetcode.dependencies.ListNode;

public class P160_IntersectionOfTwoLinkedLists {
	private static int length(ListNode node) {
		int length = 0;
		while (node != null) {
			node = node.next;
			length++;
		}
		return length;
	}

	// Solution 1
	public static ListNode getIntersectionNode_1(ListNode headA, ListNode headB) {
		int lenA = length(headA), lenB = length(headB);
		// move headA and headB to the same start point
		while (lenA > lenB) {
			headA = headA.next;
			lenA--;
		}
		while (lenA < lenB) {
			headB = headB.next;
			lenB--;
		}
		// find the intersection until end
		while (headA != headB) {
			headA = headA.next;
			headB = headB.next;
		}
		return headA;
	}

	// Solution 2
	public static ListNode getIntersectionNode_2(ListNode headA, ListNode headB) {
		if (null == headA || null == headB)
			return null;

		ListNode curA = headA, curB = headB;

		// Basically point currA to headB at the end of listA 
		// and currB to headA at the end of list B. 
		// thus the different in length will offset and we will find the common one
		while (curA != curB) {
			curA = curA == null ? headB : curA.next;
			curB = curB == null ? headA : curB.next;
		}
		return curA;
	}

	public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		return getIntersectionNode_2(headA, headB);
	}

	@Test
	public void test() {
		ListNode a1 = new ListNode(1);
		ListNode a2 = new ListNode(1);
		ListNode b1 = new ListNode(1);
		ListNode b2 = new ListNode(1);
		ListNode b3 = new ListNode(1);

		ListNode c1 = new ListNode(1);
		ListNode c2 = new ListNode(1);
		ListNode c3 = new ListNode(1);

		a1.next = a2;
		b1.next = b2;
		b2.next = b3;
		c1.next = c2;
		c2.next = c3;
		a2.next = c1;
		b3.next = c1;

		assertTrue("Test1", getIntersectionNode(a1, b1) == c1);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P160_IntersectionOfTwoLinkedLists.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
