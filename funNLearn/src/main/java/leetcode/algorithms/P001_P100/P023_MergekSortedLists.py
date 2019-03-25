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

class ListNode(object):
    """
    Singly linked list node class
    """
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_llist(r_list=[]):
        if not r_list or len(r_list)<1:
            return None

        head_node = ListNode(val=r_list[0])
        curr_node = head_node
        for nd in range (1, len(r_list)):
            new_node = ListNode(r_list[nd])
            curr_node.next = new_node
            curr_node = new_node
        return head_node

    def __str__(self):
        ret_str = ""
        curr_node = self
        while (curr_node):
            ret_str += str(curr_node.val)
            if curr_node.next:
                ret_str += " -> "
            curr_node = curr_node.next
        return ret_str

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
