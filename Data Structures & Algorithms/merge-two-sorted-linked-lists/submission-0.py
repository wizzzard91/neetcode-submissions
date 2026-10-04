# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nextA = list1
        nextB = list2

        if not nextA:
            return nextB
        if not nextB:
            return nextA


        curr = None
        if nextA.val < nextB.val:
            curr = nextA
            nextA = curr.next
        else:
            curr = nextB
            nextB = curr.next
        
        newHead = curr
        while curr:
            if not nextA:
                curr.next = nextB
                break
            if not nextB:
                curr.next = nextA
                break
            
            if nextA.val < nextB.val:
                curr.next = nextA
                curr = nextA
                nextA = curr.next
            else:
                curr.next = nextB
                curr = nextB
                nextB = curr.next

        return newHead
