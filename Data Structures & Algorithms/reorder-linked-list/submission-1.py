# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: 
            return None
        # find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second part
        prev = None
        cur = slow.next
        slow.next = None # unlink the half
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # prev now points to new start

        # merge two halfs
        l1, l2 = head, prev
        
        while l2:
            nxt1, nxt2 = l1.next, l2.next
            l1.next = l2
            l2.next = nxt1
            l1, l2 = nxt1, nxt2