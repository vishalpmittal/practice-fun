/*
 * Given a singly linked list, determine if it is a palindrome.
 * 
 * Follow up:
 * Could you do it in O(n) time and O(1) space?
 */

package leetcode;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import leetcode.dependencies.ListNode;

import static org.junit.Assert.assertTrue;

import java.util.Stack;

import static org.junit.Assert.assertFalse;

public class P234_PalindromeLinkedList {

	public static ListNode root;

	// O(n) time and O(1) space 
	// Reverse the first half of the list
	public static boolean isPalindrome_1(ListNode head) {
		if (head == null) {
			return true;
		}
		ListNode p1 = head;
		ListNode p2 = head;
		ListNode p3 = p1.next;
		ListNode pre = p1;

		//find mid pointer, and reverse head half part
		while (p2.next != null && p2.next.next != null) {
			p2 = p2.next.next;
			pre = p1;
			p1 = p3;
			p3 = p3.next;
			p1.next = pre;
		}

		//odd number of elements, need left move p1 one step
		if (p2.next == null) {
			p1 = p1.next;
		} else { //even number of elements, do nothing
		}

		//compare from mid to head/tail
		while (p3 != null) {
			if (p1.val != p3.val) {
				return false;
			}
			p1 = p1.next;
			p3 = p3.next;
		}
		return true;
	}

	// O(N) time and O(n) space 
	// Using stack
	public static boolean isPalindrome_2(ListNode head) {
		if (head == null) {
			return true;
		}

		Stack<Integer> stck = new Stack<Integer>();
		ListNode p1 = head, p2 = head;
		while (p2.next != null && p2.next.next != null) {
			stck.push(p1.val);
			p1 = p1.next;
			p2 = p2.next.next;
		}

		if (p2.next != null)
			stck.push(p1.val);
		p1 = p1.next;

		while (p1 != null) {
			if (p1.val != stck.pop())
				return false;
			else
				p1 = p1.next;
		}
		return stck.isEmpty();
	}

	// O(N) time and O(n) space 
	// Recursive solution
	public static boolean isPalindrome_3(ListNode head) {
		root = head;
		return (head == null) ? true : _isPalindrome(head);
	}

	public static boolean _isPalindrome(ListNode head) {
		boolean flag = true;
		if (head.next != null) {
			flag = _isPalindrome(head.next);
		}
		if (flag && root.val == head.val) {
			root = root.next;
			return true;
		}
		return false;
	}

	public static boolean isPalindrome(ListNode head) {
		//		return isPalindrome_1(head);
		//		return isPalindrome_2(head);
		return isPalindrome_3(head);
	}

	@Test
	public void test() {
		ListNode rn = ListNode.makeMeAList(new int[] { 1, 2, 3, 2, 1 });
		ListNode rn1 = ListNode.makeMeAList(new int[] { 1, 2, 3, 4, 5 });
		ListNode rn2 = ListNode.makeMeAList(new int[] { 1, 2, 3, 3, 2, 1 });
		assertTrue("Test1", isPalindrome(rn));
		assertFalse("Test2", isPalindrome(rn1));
		assertTrue("Test3", isPalindrome(rn2));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P234_PalindromeLinkedList.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
