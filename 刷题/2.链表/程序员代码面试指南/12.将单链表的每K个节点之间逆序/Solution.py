class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_k_node_1(head: Node, k: int):
    if k < 2:
        return head

    cur = head
    new_head = head
    pre = None
    stack = []

    while cur is not None:
        next = cur.next
        #先添加到栈中，这样第一次满足K个的时候，cur就是新的头节点
        stack.append(cur)

        if len(stack) == k:
            pre = resign_1(stack, pre, next)
            new_head = cur if new_head is None else new_head
        cur = next
    return new_head


def resign_1(stack, left, right):
    """拼接K个节点"""
    cur = stack.pop()
    if left is not None:
        left.next = cur
    while stack:
        next = stack.pop()
        cur.next = next
        cur = next
    cur.next = right
    return cur


def reverse_k_node_2(head: Node, k: int):
    if k < 2:
        return head
    cur = head
    pre = None
    count = 1
    while cur is not None:
        next = cur.next
        if count == k:
            start = head if pre is None else pre.next
            head = cur if pre is None else head
            resign_2(pre, start, cur, next)


def resign_2(left, start, end, right):
    """逆序N个节点"""
    pre = start
    cur = start.next

    while cur != right:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    if left is not None:
        left.next = end

    start.next = right
