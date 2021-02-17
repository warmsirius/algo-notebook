class Node(object):
    def __init__(self, data):
        self.right = None
        self.left = None
        self.value = data


def get_max_tree(arr):
    n_arr = [Node(i) for i in arr]
    stack = []
    # 根据单调栈解法，找到左边第1个比cur_node.value 大的值
    l_big_map = {}
    for i in range(len(n_arr)):
        cur_node = n_arr[i]
        while stack and stack[-1].value < cur_node.value:
            pop_stack_set_map(stack, l_big_map)
        stack.append(cur_node)
    while stack:
        pop_stack_set_map(stack, l_big_map)

    # 根据单调栈解法，找到右边第1个比cur_node.value 大的值
    r_big_map = {}
    for i in range(len(n_arr) - 1, -1, -1):
        cur_node = n_arr[i]
        while stack and stack[-1].value < cur_node.value:
            pop_stack_set_map(stack, r_big_map)
        stack.append(cur_node)
    while stack:
        pop_stack_set_map(stack, r_big_map)

    # 根据构造原则，来构造 MaxTree
    head = None
    for i in range(len(n_arr)):
        cur_node = n_arr[i]
        left = l_big_map.get(cur_node)
        right = r_big_map.get(cur_node)

        # case 1: 如果左右都没有比cur_node更大的node，则为 MaxTree 头节点
        if left is None and right is None:
            head = cur_node
        # case 2: 如果左边没有比cur_node更大的节点，右边有，则放入到右边节点的空子节点即可
        elif left is None:
            # 先判断左节点，原因是因为二叉树是从左到右节点的
            if right.left is None:
                right.left = cur_node
            else:
                right.right = cur_node
        # case 3: 如果右边没有比cur_node更大的节点，左边有，则放入到左边节点的空子节点即可
        elif right is None:
            # 先判断左节点，原因是因为二叉树是从左到右节点的
            if left.left is None:
                left.left = cur_node
            else:
                left.right = cur_node
        # case 4: 左右都有比cur_node更大的值，取较小的那个node作为parent，然后插入到parent节点的空子节点即可
        else:
            parent = left if left.value < right.value else right
            # 先判断左节点，原因是因为二叉树是从左到右节点的
            if parent.left is None:
                parent.left = cur_node
            else:
                parent.right = cur_node
    return head


def pop_stack_set_map(stack, map_in):
    """设置节点的左边和右边的第1个最大值"""
    pop_node = stack.pop()
    if len(stack) == 0:
        map_in[pop_node] = None
    else:
        map_in[pop_node] = stack[-1]


if __name__ == '__main__':
    assert get_max_tree([3, 4, 5, 1, 2]).value == 5
    assert get_max_tree([3, 4, 5, 1, 2]).left.value == 4
    assert get_max_tree([3, 4, 5, 1, 2]).left.left.value == 3
    assert get_max_tree([3, 4, 5, 1, 2]).left.right is None
    assert get_max_tree([3, 4, 5, 1, 2]).right.value == 2
    assert get_max_tree([3, 4, 5, 1, 2]).right.left.value == 1
    assert get_max_tree([3, 4, 5, 1, 2]).right.right is None
