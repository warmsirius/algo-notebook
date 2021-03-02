class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_node_wired(node: Node):
    if node is None:
        return None
    next = node.next
    if next is None:
        raise RuntimeError("can not remove last node.")
    node.value = next.value
    node.next = next.next
