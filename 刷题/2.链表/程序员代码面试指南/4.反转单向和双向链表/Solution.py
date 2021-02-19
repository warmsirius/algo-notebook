class SingleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


def reverse_single_link_list(head: SingleNode):
    """反转单向链表"""
    pre_node, next_node = None, None
    while head is not None:
        next_node = head.next
        head.next = pre_node

        pre_node = head
        head = next_node
    return pre_node


def reverse_double_link_list(head: DoubleNode):
    """反转双向链表"""
    prev_node, next_node = None, None
    while head is not None:
        next_node = head.next
        head.next = prev_node
        head.pre = next_node

        prev_node = head
        head = next_node
    return prev_node
