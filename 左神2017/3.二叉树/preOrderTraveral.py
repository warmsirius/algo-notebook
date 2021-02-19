from TreeNode import TreeNode


def preOrderTraveral(node: TreeNode):
    """二叉树前序遍历: 递归解法"""
    if node is None:
        return []
    # 前序遍历的打印:
    # print(node.data)
    # preOrderTraveral(node.left)
    # preOrderTraveral(node.right)
    return [node.data] + preOrderTraveral(node.left) + preOrderTraveral(node.right)


def preOrderTraveral_1(node: TreeNode):
    """二叉树前序遍历: 循环解法"""
    if node is None:
        return []

    stack = []
    result = []
    stack.append(node)

    while stack:
        node = stack.pop()
        result.append(node.data)
        # 栈特点后进先出: 所以先压入right，再压入left
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


if __name__ == "__main__":
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
    A.left, A.right = B, C
    B.right = D
    C.left, C.right = E, F
    E.left = G
    F.left, F.right = H, I
    assert preOrderTraveral(A) == ['A', 'B', 'D', 'C', 'E', 'G', 'F', 'H', 'I']
    assert preOrderTraveral_1(A) == ['A', 'B', 'D', 'C', 'E', 'G', 'F', 'H', 'I']
