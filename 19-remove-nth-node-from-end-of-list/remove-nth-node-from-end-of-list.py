# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        count = count - n + 1 
        count2 = 0 
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr:
            count2 += 1 
            if count2  == count :
                prev.next = curr.next
                break
            prev, curr = curr, curr.next
        return dummy.next
