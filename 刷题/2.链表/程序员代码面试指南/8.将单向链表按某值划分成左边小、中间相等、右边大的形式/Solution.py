class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def list_partition(head: Node, pivot: int):
    """普通解法划分链表"""
    if head is None or head.next is None:
        return head
    # 存放所有节点
    stack = []
    cur = head
    while cur is not None:
        stack.append(cur)
        cur = cur.next

    # 开始进行划分
    arr_partition(stack, pivot)

    # 重新连接节点
    for i in range(1, len(stack)):
        stack[i - 1].next = stack[i]
    stack[i] = None

    return stack[0]


def arr_partition(node_arr: Node, pivot: int):
    less = -1
    more = len(node_arr)
    index = 0
    while index < more:
        if node_arr[index] < pivot:
            # 当arr[l] < arr[r]时，less指针加1，l指针加1
            less += 1
            swap(node_arr, less, index)
            index += 1
        elif node_arr[index] == pivot:
            # 当arr[l] = arr[r]时，l指针+1，但是less指针不动
            index += 1
        else:
            # 当arr[l] > arr[r]时，和more前面的一位进行交换，然后指针均保持不动
            more -= 1
            swap(node_arr, more, index)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def list_partition_2(head: Node, pivot: int):
    """将链表划分为3部分"""
    sH, sT = None, None
    eH, eT = None, None
    bH, bT = None, None

    while head is not None:
        next = head.next
        # 先将head.next清空，下面会依次进行判断，然后重新指定next指针
        head.next = None
        if head.value < pivot:
            if sH is None:
                sH = head
                sT = head
            else:
                sH.next = head
                sT = head
        elif head.value == pivot:
            if eH is None:
                eH = head
                eT = head
            else:
                eH.next = eT
                eT = head
        else:
            if bH is None:
                bH = head
                bT = head
            else:
                bH.next = bT
                bT = head
        head = next

    # 连接三部分
    if sT is not None:
        sT.next = eH
        eT = sT if eT is None else eT

    if eT is not None:
        eT.next = bH

    return sH if (sH is None) else eH if (eH is not None) else bH
