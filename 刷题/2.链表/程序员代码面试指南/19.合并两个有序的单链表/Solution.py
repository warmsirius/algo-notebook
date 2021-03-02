class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_two_lists(head1: Node, head2: Node):
    """合并两个有序链表，新增链表结构"""
    # 哨兵节点:
    # 好处1: 便于快速找到头节点
    # 好处2: 省去处理 pre_node is None的情况
    pre_head = Node(-1)
    pre_node = pre_head
    while head1 is not None and head2 is not None:
        if head1.value <= head2.value:
            node = Node(head1.value)
            head1 = head1.next
            pre_node.next = node
        else:
            node = Node(head2.value)
            head2 = head2.next
            pre_node.next = node
        pre_node = pre_node.next

    pre_node.next = head1 if head1 else head2

    return pre_head.next


def merge_two_list_2(head1: Node, head2: Node):
    """原链表基础上进行合并"""
    if head1 is None or head2 is None:
        return head1 if head2 is None else head2

    head = head1 if head1.value < head2.value else head2
    cur1 = head1 if head == head1 else head2
    cur2 = head2 if head == head1 else head1
    pre = None

    while cur2 is not None and cur1 is not None:
        if cur1.value <= cur2.value:
            pre = cur1
            cur1 = cur1.next
        else:
            next = cur2.next
            pre.next = cur2
            cur2.next = cur1
            pre = cur2
            cur2 = next
    pre.next = cur2 if cur1 is None else cur1
    return head
