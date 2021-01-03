"""
计算1个数组中有多少个逆序对:
如: [1, 4, 3, 6, 5]

1: 0
4: 0
3: 1
6: 0
5: 1

res = 1 + 1 = 2
"""


def ReversePair(arr):
    """获取数组的逆序对"""
    if arr == [] or len(arr) < 2:
        return 0
    return mergeSort(arr, 0, len(arr) - 1)


def mergeSort(arr, l, r):
    if l == r:
        return 0
    mid = l + ((r - l) >> 1)
    return mergeSort(arr, l, mid) + mergeSort(arr, mid + 1, r) + merge(arr, l, mid, r)


def merge(arr, l, m, r):
    tmp = []
    i = 0
    p1 = l
    p2 = m + 1
    res = 0

    while p1 <= m and p2 <= r:
        if arr[p1] <= arr[p2]:
            tmp.append(arr[p1])
            p1 += 1
        else:
            res += (m - p1 + 1)
            tmp.append(arr[p2])
            p2 += 1
        i += 1

    while p1 <= m:
        tmp.append(arr[p1])
        p1 += 1
        i += 1

    while p2 <= r:
        tmp.append(arr[p2])
        p2 += 1
        i += 1

    for i in range(len(tmp)):
        arr[l + i] = tmp[i]
    return res


arr = [1, 4, 3, 6]
print(ReversePair(arr))
