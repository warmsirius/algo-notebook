class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(head: Node):
    """反转链表"""
    # 三个指针: pre_node、head、next_node
    # 步骤:【head的下一个指针】指向【pre_node】
    #     【pre_node】变为 【head】
    #     【head】变为 【next_node】
    pre_node = None
    next_node = None
    while head is not None:
        next_node = head.next
        head.next = pre_node
        pre_node = head
        head = next_node
    return pre_node
