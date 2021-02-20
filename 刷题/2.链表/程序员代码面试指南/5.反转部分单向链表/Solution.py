class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_part(head: Node, _from: int, _to: int):
    length = 0
    node1 = head
    fPre = None
    tPos = None
    while node1 is not None:
        length += 1
        fPre = node1 if length == _from - 1 else fPre
        tPos = node1 if length == _to + 1 else tPos
        node1 = node1.next
    if _from > _to or _from < 1 or _to > length:
        return head

    # 找到开始反转的点，判断是否为头节点，
    # 和之前的反转单链表一样的，node1就是之前的pre，node2相当于head，这里已经交换过1次了
    # 不一样的是这次tPos可能是None，也可能是其中1个节点，所以在while循环前已经执行了一次交换
    node1 = head if fPre is None else fPre.next
    node2 = node1.next
    node1.next = tPos

    while node2 is not None:
        next_node = node2.next
        node2.next = node1

        node1 = node2
        node2 = next_node

    if fPre is not None:
        # 如果fPre is not None, 就说明fPre这个点next点还没更改，还是之前的点
        # node1: 最后是tPos前1个节点，然后就是交换后的第1个节点，所以 fPre.next = node1
        fPre.next = node1
        return head
    # 如果fPre is None，说明head开始交换，而且head已经变成node1了
    return node1
