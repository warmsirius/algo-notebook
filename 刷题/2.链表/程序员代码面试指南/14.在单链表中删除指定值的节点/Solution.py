class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_value_1(head: Node, num: int):
    """利用栈删除重复值"""
    stack = []
    while head is not None:
        if head.value != num:
            stack.append(head)
        head = head.next

    while stack:
        stack[-1].next = head
        head = stack.pop()
    return head


def remove_value_2(head: Node, num: int):
    while head is not None:
        if head.num != num:
            break
        head = head.next
    pre = head
    cur = head
    while cur is not None:
        if cur.value == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return head
