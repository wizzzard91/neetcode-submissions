# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we need to position two pointers - one curr, one currPlusN
        curPlusN = head
        for i in range(1, n):
            curPlusN = curPlusN.next if curPlusN else None
        
        if not curPlusN:
            return head
            
        # position curr and curPlusN
        curr = head
        prev = None
        while curPlusN.next:
            prev = curr
            curr = curr.next
            curPlusN = curPlusN.next
        
        if prev:
            prev.next = curr.next
        else:
            head = head.next
        return head
