class SingleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


def remove_single_list_last_Kth_node(head: SingleNode, K: int):
    """单链表删除倒数第K个节点"""
    cur = head
    while cur is not None:
        pre = pre.next
        K -= 1

    if K > 0:
        print(f"不存在倒数第{K}个节点")
    elif K == 0:
        head = head.next
    else:
        while K != 0:
            cur = head
            cur = cur.next
            K += 1

        cur.next = cur.next.next
    return head


def remove_double_list_last_Kth_node(head: DoubleNode, K: int):
    """双链表删除倒数第K个节点"""
    cur = head
    while cur is not None:
        cur = cur.next
        K -= 1
    if K > 0:
        print(f"不存在倒数第{K}个节点")
    elif K == 0:
        head = head.next
        head.pre = None
    else:
        cur = head
        while K != 0:
            cur = cur.next
            K += 1
        new_node = cur.next.next
        cur.next = new_node
        if new_node is not None:
            new_node.pre = cur
    return head
