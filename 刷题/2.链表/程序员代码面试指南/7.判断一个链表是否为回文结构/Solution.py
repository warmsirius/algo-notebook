class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def is_palindrome_1(head: Node):
    """用栈的思路结果"""
    stack = []
    cur = head
    while cur is not None:
        stack.append(cur)
        cur = cur.next

    while head is not None:
        if head.value != stack.pop().value:
            return False
        head = head.next
    return True


def is_palindrome_2(head: Node):
    if head is None or head.next is None:
        return True

    cur = head
    right = head.next

    while cur.next is not None and cur.next.next is not None:
        pre = pre.next
        cur = cur.next.next

    stack = []
    right = right.next
    while right is not None:
        stack.append(right)
        right = right.next

    while stack:
        if head.value != stack.pop().value:
            return False
        head = head.next
    return True


def is_palindrome_3(head: Node):
    """三个变量完成判断"""
    if head is None or head.next is None:
        return True
    n1 = head
    cur = head
    while cur.next is not None and cur.next.next is not None:
        n1 = n1.next
        cur = cur.next

    # 右边第1个节点
    n1.next = None
    cur = n1.next
    # 开始反转right 到 最后一个节点
    while cur is not None:
        next = cur.next
        cur.next = n1
        n1 = cur  # 就是最后1个节点
        cur = next

    n3 = n1
    n2 = head
    res = True
    while n2 is not None and n3 is not None:
        if n2.value != n3.value:
            res = False
        n2 = n2.next
        n3 = n3.next

    # 还原链表，从mid到尾节点开始反转
    n3 = None
    while n1 is not None:
        next = n1.next
        n1.next = n3
        n3 = n1
        n1 = next
    return res
