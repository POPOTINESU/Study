from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first, second = dummy, dummy

        for _ in range(n + 1):
            if first:
                first = first.next

        while first and second:
            first = first.next
            second = second.next

        if second and second.next:
            second.next = second.next.next

        return dummy.next
