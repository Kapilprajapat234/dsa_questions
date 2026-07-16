# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        new_head = None
        curr = head

        while curr:
            new_node = ListNode(curr.val)   
            new_node.next = new_head       
            new_head = new_node             
            curr = curr.next
        while head and new_head:
            if head.val != new_head.val:
                return False

            head = head.next
            new_head = new_head.next

        return head is None and new_head is None                
