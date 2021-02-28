class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_rep_1(head: Node):
    if head is None:
        return head

    node_set = set()
    pre = head
    cur = head.next
    node_set.add(head.value)
    while cur is not None:
        next = cur.next
        if cur.value in node_set:
            # 删除当前节点
            pre.next = cur.next
        else:
            # 如果不是的话，pre指向当前指针
            node_set.add(cur.value)
            pre = cur
        cur = next
    return head


def remove_rep_2(head: Node):
    cur = head
    while cur is not None:
        pre = cur
        next = cur.next
        # 查看next有没有重复的
        while next is not None:
            if cur.value == next.value:
                pre.next = next.next
            else:
                pre = next
            next = next.next
        cur = cur.next
    return head