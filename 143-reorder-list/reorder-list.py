# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        pre = None 
        curr = slow 
        while curr:
            nxt = curr.next 
            curr.next = pre
            pre = curr
            curr = nxt 

        dummy = ListNode()
        tail = dummy 
        while head and pre :
            next_head = head.next
            next_pre = pre.next

            tail.next = head 
            head = next_head
            tail = tail.next

            tail.next = pre
            pre = next_pre
            tail = tail.next 

        tail.next = head if head else pre 
    