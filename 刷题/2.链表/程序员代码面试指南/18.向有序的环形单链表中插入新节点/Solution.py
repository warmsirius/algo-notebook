class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_num(head: Node, num: int):
    node = Node(num)

    if head is None:
        node.next = node
    pre = head
    cur = head.next
    while cur != head:
        if pre.value <= num and cur.value >= num:
            break
        pre = cur
        cur = cur.next
    pre.next = node
    node.next = cur
