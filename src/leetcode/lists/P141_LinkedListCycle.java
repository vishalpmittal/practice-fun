/**
 *  Given a linked list, determine if it has a cycle in it.
 *  
 *  Follow up:
 *  Can you solve it without using extra space?
 */
package leetcode.lists;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.HashSet;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import leetcode.dependencies.ListNode;

public class P141_LinkedListCycle {

	// Using HashSet.O(n) time and O(n) space
	public static boolean hasCycle(ListNode head) {
		if (head == null || head.next == null)
			return false;

		HashSet<ListNode> holder = new HashSet<ListNode>();
		ListNode curr = head;
		while (curr != null) {
			if (!holder.add(curr))
				return true;
			curr = curr.next;
		}
		return false;
	}

	// Using no extra space
	public static boolean hasCycle_1(ListNode head) {
		if (head == null || head.next == null)
			return false;

		ListNode leader = head;
		ListNode follower = head;

		while (leader.next != null && leader.next.next != null) {
			leader = leader.next.next;
			follower = follower.next;
			if (leader == follower)
				return true;
		}
		return false;
	}

	@Test
	public void test() {
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

		assertFalse("Test1", hasCycle(ln1));

		ln5.next = ln3;
		assertTrue("Test2", hasCycle(ln1));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P141_LinkedListCycle.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
