class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def get_loop_node(head: Node):
    if head is None or head.next is None or head.next.next is None:
        return None

    n1 = head.next
    n2 = head.next.next
    while n1 != n2:
        if n2.next is None or n2.next.next is None:
            return None
        n2 = n2.next.next
        n1 = n1.next

    n2 = head
    while n1 != n2:
        n1 = n1.next
        n2 = n2.next
    return n1


def no_loop(head1: Node, head2: Node):
    if head1 is None or head2 is None:
        return None
    cur1 = head1
    cur2 = head2

    n = 0
    while cur1.next is not None:
        n += 1
        # cur1就是head1的最后1个节点
        cur1 = cur1.next

    while cur2.next is not None:
        n -= 1
        # cur2就是head2的最后1个节点
        cur2 = cur2.next

    # 如果最后1个节点不相等，那么就一定不相交
    if cur1 != cur2:
        return None

    cur1 = head1 if n > 0 else head2
    cur2 = head1 if cur1 == head2 else head2
    n = abs(n)
    while n != 0:
        n -= 1
        cur1 = cur1.next

    # 肯定至少会在end1和end2的结尾结束的
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1


def both_loop(head1: Node, loop1: Node, head2: Node, loop2: Node):
    if loop1 == loop2:
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1 != loop1:
            n += 1
            cur1 = cur1.next
        while cur2 != loop2:
            n -= 1
            cur2 = cur2.next

        cur1 = head1 if n > 0 else head2
        cur2 = head1 if cur1 == head1 else head2
        n = abs(n)
        while n != 0:
            n -= 1
            cur1 = cur1.next

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return cur1
            cur1 = cur1.next

        return None


def get_intersect_node(head1: Node, head2: Node):
    if head1 is None or head2 is None:
        return None
    loop1 = get_loop_node(head1)
    loop2 = get_loop_node(head2)
    if loop1 is None and loop2 is None:
        return no_loop(head1, head2)
    elif loop1 is not None and loop2 is not None:
        return both_loop(head1, loop1, head2, loop2)
    else:
        return None
