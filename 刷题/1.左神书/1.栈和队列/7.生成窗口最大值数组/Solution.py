from collections import deque


def getMaxWindow(arr, w):
    """生成窗口最大值数组"""
    if arr == [] or w < 1 or len(arr) < w:
        return None
    import pdb; pdb.set_trace()
    # 双端队列: qmax，记录每个窗口的最大值下标
    qmax = deque()
    res = [0] * (len(arr) - w + 1)
    index = 0
    for i in range(len(arr)):
        while qmax and arr[qmax[-1]] <= arr[i]:
            qmax.pop()
        qmax.append(i)

        if qmax[0] == i - w:
            # qmax[0] == i - w，说明: qmax[0] 超出了 以i为右边界的长度w窗口的范围
            # 在每次滑动窗口赋值前，应该将w窗口左边界外的元素提出
            qmax.popleft()
        if i >= w - 1:
            # i >= w - 1
            # i == w - 1: 此时已经将 第一个w窗口 走完了，qmax[0] 一定是第1个w窗口的最大值，所以直接赋值即可
            # i > w - 1: 此时每个i都是 一个w窗口(以i为右边界的w窗口，上一步将不在这个滑动窗口的值去掉了)，所以qmax[0]为该w窗口的最大值
            res[index] = arr[qmax[0]]
            index += 1
    return res


if __name__ == "__main__":
    assert getMaxWindow([4, 3, 5, 4, 3, 3, 6, 7], 3) == [5, 5, 5, 4, 6, 7]
