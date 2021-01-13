def getAndRemoveLastElement(stack):
    """移除并返回栈底元素"""
    result = stack.pop()
    if not stack:
        return result
    else:
        last = getAndRemoveLastElement(stack)
        stack.append(result)
        return last


def reverse(stack):
    """逆序一个栈"""
    if not stack:
        return
    i = getAndRemoveLastElement(stack)
    stack.append(i)
