from TreeNode import TreeNode


def postOrderTraveral(node: TreeNode):
    """后序遍历: 递归实现"""
    if node is None:
        return []
    return postOrderTraveral(node.left) + postOrderTraveral(node.right) + [node.data]


def postOrderTraveral_1(node: TreeNode):
    """后序遍历: 迭代实现"""
    if node is None:
        return []

    stack = [node]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.data)
        # 栈特点后进先出: 所以先压入left，再压入right，这样就是 根->右->左，取反就是左->右->根
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


if __name__ == "__main__":
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
    A.left, A.right = B, C
    B.right = D
    C.left, C.right = E, F
    E.left = G
    F.left, F.right = H, I
    assert postOrderTraveral(A) == ['D', 'B', 'G', 'E', 'H', 'I', 'F', 'C', 'A']
    assert postOrderTraveral_1(A) == ['D', 'B', 'G', 'E', 'H', 'I', 'F', 'C', 'A']
