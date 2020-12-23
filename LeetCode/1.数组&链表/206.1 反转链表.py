class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList1(head: ListNode):
    prev, cur = None, head
    while cur is not None:
        nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode


def reverseList2(head: ListNode):
    if head is None or head.next is None: return head
    newList = reverseList2(head.next)
    head.next.next = head
    head.next = None
    return newList
