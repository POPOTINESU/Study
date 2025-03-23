from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = self.reverseLinkedList(slow.next)
        slow.next = None
        
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
    
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        return prev