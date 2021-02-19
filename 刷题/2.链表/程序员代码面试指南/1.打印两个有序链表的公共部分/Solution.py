class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def print_common_part(head1: Node, head2: Node):
    """打印两个有序链表的公共部分"""
    while head1 is not None and head2 is not None:
        if head1.value == head2.value:
            print(f"公共节点: {head1.value}")
            head1 = head1.next
            head2 = head2.next
        elif head1.value > head2.value:
            head2 = head2.next
        else:
            head1 = head1.next


if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(4)

    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(4)

    print_common_part(head1, head2)
