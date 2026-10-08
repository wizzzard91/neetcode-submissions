# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        first, second = dummy, dummy
        for i in range(0, n):
            second = second.next

        while second.next:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        return dummy.next
