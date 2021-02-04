#
# Created by 袁俊 on 2021/01/16.
#


def rightWay(arr):
    """每个位置分别向左和向右遍历一下，O(N2)"""
    res = [[]] * len(arr)
    for i in range(len(arr)):
        leftLessIndex = -1
        rightLessIndex = -2
        cur = i - 1
        while cur >= 0:
            if arr[cur] < arr[i]:
                leftLessIndex = cur
                break
            cur -= 1
        cur = cur + 1
        while cur < len(arr):
            if arr[cur] < arr[i]:
                rightLessIndex = cur
                break
            cur += 1
        res[i][0] = leftLessIndex
        res[i][1] = rightLessIndex
    return res


def getNearLessNoRepeat(arr):
    """利用栈解决，O(N)"""
    res = [[]] * len(arr)
    stack = []
    for i in range(len(arr)):
        # stack的栈顶元素 大于 当前元素，说明当前元素是这个栈顶右边的第1个小的元素
        while (len(stack)) and (arr[stack[-1]] > arr[i]):
            popIndex = stack.pop()
            leftLessIndex = stack[-1] if len(stack) else -1
            res[popIndex][0] = leftLessIndex
            res[popIndex][1] = i
        stack.append(i)
        while len(stack):
            popIndex = stack.pop()
            leftLessIndex = stack[-1] if len(stack) else -1
            res[popIndex][0] = leftLessIndex
            res[popIndex][1] = -1
        return res


def getNearLess(arr):
    res = [[-2, -2]] * len(arr)
    pass
