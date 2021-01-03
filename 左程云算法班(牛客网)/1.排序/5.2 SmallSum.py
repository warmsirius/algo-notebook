"""
小和问题:

如: [3, 5, 1, 4, 6]
3: 0
5: 3 = 3
1: 0
4: 3 + 1 = 4
6: 3 + 5 + 4 + 1 = 13

res = 13 + 4 + 3 = 20
"""


def smallSum(arr):
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
        if arr[p1] < arr[p2]:
            tmp.append(arr[p1])
            res += (r - p2 + 1) * arr[p1]
            p1 += 1
        else:
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


arr = [3, 5, 1, 4, 6]
print(smallSum(arr))
