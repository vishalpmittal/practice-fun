"""
    Tag: bit, linked list

    Given head which is a reference node to a singly-linked list. 
    The value of each node in the linked list is either 0 or 1. 
    The linked list holds the binary representation of a number.
    Return the decimal value of the number in the linked list.

    Example 1: Input: head = [1,0,1] Output: 5
    Explanation: (101) in base 2 = (5) in base 10

    Example 2: Input: head = [0] Output: 0 
    Example 3: Input: head = [1] Output: 1
    Example 4: Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0] Output: 18880
    Example 5: Input: head = [0,0] Output: 0

    Constraints:
    -  The Linked List is not empty.
    -  Number of nodes will not exceed 30.
    -  Each node's value is either 0 or 1.
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return sum([l[i]*(2**(len(l)-i-1)) for i in range(len(l)-1, -1, -1)])

    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = (ans << 1) | head.val
            head = head.next
        return ans


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

assert Solution().getDecimalValue(head) == 5
print('Tests Passed!!')
