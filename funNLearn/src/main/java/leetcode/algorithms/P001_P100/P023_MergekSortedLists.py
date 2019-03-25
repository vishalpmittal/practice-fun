"""
    Tag: linked list, bfs, sort
        
    Merge k sorted linked lists and return it as one sorted list. 
    Analyze and describe its complexity.

    Example:
    Input:
    [
        1->4->5,
        1->3->4,
        2->6
    ]
    Output: 1->1->2->3->4->4->5->6
"""
from Queue import PriorityQueue

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'dependencies'))
from list_node import ListNode

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        
        # add the first nodes from all the list to priority queue
        # This insures the smallest node of all the lists are already in queue
        for node in lists:
            if node:
                q.put((node.val,node))

        while q.qsize()>0:
            # get the smallest one from priority queue
            curr.next = q.get()[1]

            # if it has a valid next add that to queue as well 
            curr=curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))

        return dummy.next

def test_code():
    obj = Solution()
    print obj.mergeKLists([
        ListNode.create_llist([1, 4, 5]),
        ListNode.create_llist([1, 3, 4]),
        ListNode.create_llist([2, 6])
    ])

test_code()
