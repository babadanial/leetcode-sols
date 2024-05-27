from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # move slow to the middle of the list
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        #  NOTE: slow, the midpoint, is always considered part of the first half of the list
        current = slow.next
        slow.next = None
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # note at the end of this loop, 
        #  - current points to None
        #  - prev points to first element in reversed list 
        #      (i.e. element n in original list)

        left = head
        right = prev
        while left and right:
            oldNextLeft = left.next
            oldNextRight = right.next

            left.next = right
            right.next = oldNextLeft

            left = oldNextLeft
            right = oldNextRight