class Node(object):
    def __init__(self, value):
        self.value = value
        self.rand = None
        self.next = None


def copy_list_with_rand_1(head: Node):
    """借助哈希表完成复制"""
    node_map = {}
    cur = head
    while cur is not None:
        node_map[cur] = Node(cur.value)
        cur = cur.next

    cur = head
    while cur is not None:
        node_map.get(cur).next = node_map.get(cur.next)
        node_map.get(cur).rand = node_map.get(cur.rand)

    return node_map.get(head)


def copy_list_with_rand_1(head: Node):
    """进阶解法: 使用变量完成"""
    if head is None:
        return head
    cur = head
    while cur is not None:
        next = cur.next
        cur.next = Node(cur.value)
        cur.next.next = next
        cur = next

    cur = head
    while cur is not None:
        next = cur.next.next
        curCopy = cur.next
        curCopy.rand = cur.rand.next if cur.rand is not None else None
        cur = next
    res = head.next
    cur = head

    # 拆分
    while cur is not None:
        next = cur.next.next
        curCopy = cur.next
        curCopy.next = next.next if next is not None else None
        cur = next
    return res
