/**
 * You are given two linked lists representing two non-negative numbers. 
 * The digits are stored in reverse order and each of their nodes contain 
 * a single digit. Add the two numbers and return it as a linked list.
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 */

package leetcode;
import leetcode.dependencies.ListNode;

public class P002_AddTwoNumbers {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode returnHead = new ListNode(0);
		ListNode resCurr = returnHead;

		ListNode l1curr = l1;
		ListNode l2curr = l2;
		int carryOver = 0;

		while (l1curr != null || l2curr != null) {
			int sum = carryOver;
			if (l1curr != null){
				sum += l1curr.val;
				l1curr = l1curr.next;				
			}
				
			if (l2curr != null){
				sum += l2curr.val;
				l2curr = l2curr.next;				
			}
			
			resCurr.next = new ListNode(sum % 10);
			resCurr = resCurr.next;
			carryOver = sum / 10;
		}

		if (carryOver != 0){
			resCurr.next = new ListNode(carryOver);
			resCurr = resCurr.next;
		}
		
		resCurr = returnHead;
		returnHead = returnHead.next;
		resCurr.next = null;
		resCurr = null;
		return returnHead;
	}

	public static void main(String[] args) {

	}

}
