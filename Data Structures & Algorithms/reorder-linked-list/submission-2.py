# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None 
        
        # requires 3 technics: find middle of LL, reverse second half, merge two lists in-place
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # prev has new head

        l1, l2 = head, prev
        while l2:
            l1next = l1.next
            l2next = l2.next
            l1.next = l2
            l2.next = l1next
            l1 = l1next
            l2 = l2next
