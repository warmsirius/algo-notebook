class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def swap_pairs(head: Node):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    while head is not None and head.next is not None:
        # 两两交换2个节点
        # 例如: 0 -> 1 -> 2 -> 3 -> 4
        next = head.next
        # Step 1: 1 -> 3
        head.next = next.next
        # Step 2: 2 -> 1
        next.next = head
        # Step 3: 0 -> 2
        prev.next = next

        # prev要交换的2个节点的前一个节点: 变更为 head: 1
        prev = head
        # head节点向前移动1位: 3
        head = head.next
    return dummy.next
