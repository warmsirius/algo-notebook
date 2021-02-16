# @author: warmsirius
# @date: 2021/02/16


def rightWay(arr):
    """暴力法: 每个位置分别向左和向右遍历一下，O(N2)"""
    res = [[-2, -2] for _ in range(len(arr))]
    for i in range(len(arr)):
        leftLessIndex = -1
        rightLessIndex = -1
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
    """无重复值数组，O(N)"""
    res = [[-2, -2] for _ in range(len(arr))]
    stack = []
    for i in range(len(arr)):
        # stack的栈顶元素 大于 当前元素，说明当前元素是这个栈顶右边的第1个小的元素
        while len(stack) and arr[stack[-1]] > arr[i]:
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
    """含重复值数组"""
    res = [[-2, -2] for _ in range(len(arr))]
    stack = []
    for i in range(len(arr)):
        while len(stack) and arr[stack[-1][0]] > arr[i]:
            popIs = stack.pop()
            leftLessIndex = stack[-1][len(stack[-1]) - 1] if len(stack) else -1
            for popi in popIs:
                res[popi][0] = leftLessIndex
                res[popi][1] = i
        if len(stack) and arr[stack[-1][0]] == arr[i]:
            stack[-1].append(i)
        else:
            li = list()
            li.append(i)
            stack.append(li)

    while len(stack):
        popIs = stack.pop()
        leftLessIndex = stack[-1][len(stack[-1]) - 1] if len(stack) else -1
        for popi in popIs:
            res[popi][0] = leftLessIndex
            res[popi][1] = -1
    return res


if __name__ == '__main__':
    arr = [3, 4, 1, 5, 6, 2, 7]
    assert getNearLessNoRepeat(arr) == [[-1, 2], [0, 2], [-1, -1], [2, 5], [3, 5], [2, -1], [5, -1]]
    arr = [3, 1, 3, 4, 3, 5, 3, 2, 2]
    assert getNearLess(arr) == [[-1, 1], [-1, -1], [1, 7], [2, 4], [1, 7], [4, 6], [1, 7], [1, -1], [1, -1]]
