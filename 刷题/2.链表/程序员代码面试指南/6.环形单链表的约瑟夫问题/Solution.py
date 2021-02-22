class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def josephus_kill(head: Node, m: int):
    """约瑟夫环问题O(Nxm)"""
    if head is None or head.next == head:
        return head

    # 找到当前节点的上一个节点，便于移除当前节点
    last = head
    while last.next != head:
        last = last.next

    # 每数到3就移除该节点
    count = 1
    while head != last:
        if count == m:
            last.next = head.next
            count = 1
        else:
            last = last.next
        head = last.next
    return head


def josephus_kill_1(head: Node, m: int):
    # 待做: 还未理解
    pass
