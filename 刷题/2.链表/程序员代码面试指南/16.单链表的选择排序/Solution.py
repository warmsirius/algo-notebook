class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def selection_sort(head: Node):
    tail = None #排序部分尾部
    cur = head #未排序部分头部
    smallPre = None #最小节点的前一个节点
    small = None #最小的节点

    while cur is not None:
        small = cur
        smallPre = get_small_pre_node(cur)
        # smallPre=None，说明small就是cur节点
        if smallPre is not None:
            small = smallPre.next
            smallPre.next = small.next

        cur = cur.next if cur == small else cur
        if tail is None:
            head = small
        else:
            tail.next = small
        return head


def get_small_pre_node(head: Node):
    smallPre = None
    small = head
    pre = head
    cur = head.next
    while cur is not None:
        if cur.value < small.value:
            smallPre = pre
            small = cur
        pre = cur
        cur = cur.next
    return smallPre
