/*
 * Write a function to delete a node (except the tail) in a singly linked list, 
 * given only access to that node.
 * 
 * Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third 
 * node with value 3, the linked list should become 1 -> 2 -> 4 after 
 * calling your function.
 * 
 */

package leetcode;

import leetcode.dependencies.ListNode;

public class P237_DeleteNodeInALinkedList {
    
	public static void deleteNode(ListNode node) {
		if (node == null)
				return;
        if(node.next!=null){
        	node.val = node.next.val;
        	node.next = node.next.next;
        }
    }
    
	public static void main(String[] args) {
		ListNode ln1 = new ListNode(1);
		ListNode ln2 = new ListNode(2);
		ListNode ln3 = new ListNode(3);
		ListNode ln4 = new ListNode(4);
		
		ln1.next = ln2;
		ln2.next = ln3;
		ln3.next = ln4;
		
		System.out.println(ListNode.getListString(ln1));
		deleteNode(ln3);
		System.out.println(ListNode.getListString(ln1));
	}

}
