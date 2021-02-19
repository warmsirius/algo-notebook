from TreeNode import TreeNode


def inOrderTraveral(node: TreeNode):
    """中序遍历: 递归方式"""
    if node is None:
        return []
    return inOrderTraveral(node.left) + [node.data] + inOrderTraveral(node.right)


def inOrderTraveral_1(root: TreeNode):
    """中序遍历: 迭代方式"""
    if root is None:
        return []
    stack = []
    result = []
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
    return result


if __name__ == "__main__":
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
    A.left, A.right = B, C
    B.right = D
    C.left, C.right = E, F
    E.left = G
    F.left, F.right = H, I
    print(inOrderTraveral(A))
    assert inOrderTraveral(A) == ['B', 'D', 'A', 'G', 'E', 'C', 'H', 'F', 'I']
    print(inOrderTraveral_1(A))