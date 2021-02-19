class SingleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


def reverse_single_link_list(head):
    """反转单链表"""
    # 三个指针: pre_node、next_node、head
    # 步骤: 每次让【head指向的节点】指向【pre指向的节点】，然后遍历，即可完成。
    pre_node = None
    next_node = None
    while head is not None:
        next_node = head.next
        # head节点的next指针指向pre_node
        head.next = pre_node
        # pre_node为当前的节点
        pre_node = head
        # head往下移动1个节点
        head = next_node
    return pre_node


def reverse_double_link_list(head):
    """反转双链表"""
    # 三个指针: pre_node、next_node、head
    # 步骤: 每次让【head下一个节点】指向【pre指向的节点】【head上一个节点】指向【next_node节点】，然后遍历，即可完成。
    pre_node = None
    next_node = None
    while head is not None:
        next_node = head.next
        head.next = pre_node
        # head的pre指针指向，当前节点的下一个节点 next_node
        head.pre = next_node
        pre_node = head
        head = next_node
    return pre_node