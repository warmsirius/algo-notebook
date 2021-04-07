from queue import Queue

class Node:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None


def serialByPre(head: Node):
    if head is None:
        return "#!"
    res = f"{head.value}!"
    res += serialByPre(head.left)
    res += serialByPre(head.right)
    return res


def reconByPreOrder(preStr):
    values = preStr.split(",")
    q = Queue()
    for i in range(len(values)):
        q.put(values[i])
    return reconPreOrder(q)

def reconPreOrder(q):
    val = q.get()
    if val == "#":
        return None
    head = Node(val)
    head.left = reconPreOrder(q)
    head.right = reconPreOrder(q)
    return head


from queue import Queue


def serialByLevel(head: Node):
    """先序遍历序列化二叉树"""
    if head is None: return "#!"

    res = f"{head.value}!"
    q = Queue()
    q.put(head)
    while q:
        node = q.get()
        if node.left is not None:
            res += f"{node.left.val}!"
            q.put(node.left)
        else:
            res += "#!"
        if node.right is not None:
            q.put(node.right)
        else:
            res += "#!"
        return res

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node7 = Node(7)
# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
# node3.right = node7
#
# print(serialByLevel(node1))
#
# sorted()
# list.sort()

from queue import Queue

import math
math.pow()
