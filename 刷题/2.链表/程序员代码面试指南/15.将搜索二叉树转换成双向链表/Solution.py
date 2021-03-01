import queue


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def convert_1(head: Node):
    node_q = queue.Queue()
    in_order_to_queue(head, node_q)
    head = node_q.get()
    pre = head
    while node_q is not None:
        cur = node_q.get()
        pre.right = cur
        cur.left = pre
        pre = cur
    pre.right = None
    return head


def in_order_to_queue(head, node_q):
    if head is None:
        return None
    in_order_to_queue(head.left, queue)
    in_order_to_queue(head)
    in_order_to_queue(head.right, node_q)


class RetrunType(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def convert_2(head: Node):
    if head is None:
        return None
    else:
        return process(head).start


def process(head: Node):
    if head is None:
        return RetrunType(None, None)
    left_list = process(head.left)
    right_list = process(head.right)

    if left_list.end is not None:
        left_list.end.right = head
    head.left = left_list.end
    head.right = right_list.start
    
    if right_list.start is None:
        right_list.start.left = head

    return RetrunType(left_list.start if left_list.start is not None else head,
                      right_list.end if right_list.end is not None else head)
