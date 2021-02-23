class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def add_list_1(head1: Node, head2: Node) -> Node:
    s1, s2 = [], []
    while head1 is not None:
        s1.append(head1.value)
        head1 = head2.next
    while head2 is not None:
        s2.append(head2.value)
        head2 = head2.next

    ca = 0
    pre = None
    while s1 or s2:
        n1 = s1.pop() if s1 else 0
        n2 = s2.pop() if s2 else 0
        n = ca + n1 + n2
        node = Node(n % 10)
        ca = n // 10
        node.next = pre
        pre = node

    if ca == 1:
        node = Node(1)
        node.next = pre
    return node


def add_list_2(head1: Node, head2: Node) -> Node:
    head1 = reverse_list(head1)
    head2 = reverse_list(head2)

    ca = 0
    c1 = head1
    c2 = head2
    pre = None
    while c1 is not None or c2 is not None:
        n1 = c1.value if c1 is not None else 0
        n2 = c2.value if c2 is not None else 0
        n = n1 + n2 + ca
        node = Node(n % 10)
        node.next = pre
        ca = n // 10
        pre = node
        c1 = c1.next if c1 is not None else None
        c2 = c2.next if c2 is not None else None

    if ca == 1:
        pre = node
        node = Node(1)
        node.next = pre

    # head1 head2 恢复原状
    reverse_list(head1)
    reverse_list(head2)

    return node


def reverse_list(head: Node):
    pre = None
    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre
