
class ListNode(object):
    """
    Singly linked list node class
    """
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

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

    @staticmethod
    def compare_llists(list1_node, list2_node):
        while list1_node or list2_node:
            if not list1_node or not list2_node or list1_node.val != list2_node.val:
                return False
            list1_node = list1_node.next
            list2_node = list2_node.next

        return True
