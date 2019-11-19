"""
    Tag: linked list, recursive
    
    Given a linked list, reverse the nodes of a linked list k at 
    a time and return its modified list.

    k is a positive integer and is less than or equal to the length 
    of the linked list. If the number of nodes is not a multiple of k 
    then left-out nodes in the end should remain as it is.

    Example:
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5

    Note:
    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'dependencies'))
from list_node import ListNode

class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            # use r to locate the range
            while r and count < k:
                r = r.next
                count += 1
            # if size k satisfied, reverse the inner linked list
            if count == k:
                pre, cur = r, l

                # standard reversing
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                
                # connect two k-groups
                jump.next, jump, l = pre, l, r

            else:
                return dummy.next


    def reverseKGroup_rec(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1

        if count < k: 
            return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup_rec(new_head, k)
        return prev

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)

def test_code():
    obj = Solution()
    test_llist = ListNode.create_llist([1, 2, 3, 4, 5])
    ans = ListNode.create_llist([2, 1, 4, 3, 5])
    
    assert ListNode.compare_llists(
        obj.reverseKGroup(test_llist, 2),
        ans
    )
    
    test_llist = ListNode.create_llist([1, 2, 3, 4, 5])
    ans = ListNode.create_llist([3, 2, 1, 4, 5])

    assert ListNode.compare_llists(
        obj.reverseKGroup(test_llist, 3),
        ans
    )

    print ("Tests Passed!")

test_code()
