# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head is not None and head.next is not None:
            next = head.next
            head.next = next.next
            next.next = head
            prev.next = next

            prev = head
            head = head.next
        return dummy.next
