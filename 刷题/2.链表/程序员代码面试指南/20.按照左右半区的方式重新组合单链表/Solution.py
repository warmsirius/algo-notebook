class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def relocate(head: Node):
    # 先分成左右2段
    if head is None or head.next is None:
        return head
    mid = head
    right = head.next
    while right.next is not None and right.next.next is not None:
        right = right.next.next
        mid = mid.next
    mid.next = None
    mergeLR(head, right)


def mergeLR(left: Node, right: Node):
    # 重新组合左右2端
    while left.next is not None:
        next = right.next
        right.next = left.next
        left.next = right
        left = right.next
    right = next
    left.next = right
