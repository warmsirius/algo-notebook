from collections import deque


def getNum(arr, num):
    if len(arr) == 0 or arr is None:
        return 0
    # 最大值的双端队列
    qmax = deque()
    # 最小值的双端队列
    qmin = deque()

    i = 0
    j = 0
    res = 0
    while i < len(arr):
        while j < len(arr):
            while len(qmin) and qmin[-1] >= arr[j]:
                qmin.pop()
            qmin.append(j)
            while len(qmax) and qmax[-1] <= arr[j]:
                qmax.pop()
            qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j += 1
        if qmin[0] == i:
            qmin.popleft()
        if qmax[0] == i:
            qmax.popleft()
        res += j - i
        i += 1
    return res
