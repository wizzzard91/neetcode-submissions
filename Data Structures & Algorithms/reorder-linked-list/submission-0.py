# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # position the pointers
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = slow.next
        slow.next = None

        # reverse second half
        prev, curr = None, secondHalf

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        secondHalf = prev

        # merge two parts
        dummy = ListNode()
        tail = dummy
        p1, p2 = head, secondHalf
        while p1 and p2:
            tail.next = p1
            p1 = p1.next
            tail = tail.next
            tail.next = p2
            p2 = p2.next
            tail = tail.next
        if p1:
            tail.next = p1
        elif p2:
            tail.next = p2
