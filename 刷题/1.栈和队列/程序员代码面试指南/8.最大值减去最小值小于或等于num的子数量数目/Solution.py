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

            # max-min > num，i往右移动1位，当前循环退出
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            # 如果满足条件，那就j继续往右移动
            j += 1

        # i应该往右移动1位，将qmax、qmin中的i删除
        if qmin[0] == i:
            qmin.popleft()
        if qmax[0] == i:
            qmax.popleft()
        # res = (j-1) - i + 1 = j - i
        res += j - i
        i += 1
    return res


if __name__ == '__main__':
    getNum([], 1)