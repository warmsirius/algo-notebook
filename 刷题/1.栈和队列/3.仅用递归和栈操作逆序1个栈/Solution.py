def getAndRemoveLastElement(stack):
    """移除并返回最后1个元素"""
    # 每次移除最后1个元素，并返回最后1个元素
    result = stack.pop()
    if not stack:
        return result
    else:
        last = getAndRemoveLastElement(stack)
        stack.append(result)
        return last


def reverse(stack):
    """逆序一个栈操作"""
    # 移除的最后1个元素，应该最后加入栈顶
    # 所以这里还需要1个递归
    if not stack:
        return
    i = getAndRemoveLastElement(stack)
    reverse(stack)
    stack.append(i)


# 关于递归心得: 分析递归栈，然后再去看步骤，这样才是最准确的，直接想比较麻烦。


if __name__ == "__main__":
    stack = [1, 2, 3, 4]
    reverse(stack)
    assert stack == [4, 3, 2, 1]
    stack = []
    reverse(stack)
    assert stack == []
