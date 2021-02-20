class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_mid_node(head: Node):
    """删除链表中间节点"""
    # 链表长度为1或者0的时，直接返回链表值
    if head is None or head.next is None:
        return head
    # 链表长度为2时，删除第1个节点
    if head.next.next is None:
        return head.next

    # pre指针: 指向要被删除的节点的上1个节点
    pre = head
    # cur指针: 一开始在pre指针的后2步，然后cur每走2步，pre走一步
    cur = head.next.next

    while cur.next is not None and cur.next.next is not None:
        pre = head.next
        cur = cur.next.next
    # 删除中间节点
    pre.next = pre.next.next
    return head


def remove_by_ratio(head: Node, a: int, b: int):
    """按比例删除节点"""
    cur = head
    length = 0
    while cur is not None:
        cur = cur.next
        length += 1

    if a < 1 or a > b: return head

    import math
    n = int(math.ceil((a * length) / b))
    print(f"n 为 {n}")

    if n == 1:
        head = head.next
    if n > 1:
        cur = head
        while n - 1 != 1:
            cur = cur.next
            n -= 1
        cur.next = cur.next.next
    return head


if __name__ == '__main__':
    head = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node2.next = node3
    node1.next = node2
    head.next = node1
    head = remove_mid_node(head)

    while head is not None:
        print(head.value)
        head = head.next

    head = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node2.next = node3
    node1.next = node2
    head.next = node1
    head = remove_by_ratio(head, 4, 4)
    while head is not None:
        print(head.value)
        head = head.next
