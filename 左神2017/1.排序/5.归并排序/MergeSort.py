def mergeSort(arr):
    if arr == [] or len(arr) < 2:
        return
    mergesort(arr, 0, len(arr) - 1)


def mergesort(arr, l, r):
    if l == r:
        return
    mid = l + ((r - l) >> 1)
    # 先处理左边部分
    mergesort(arr, l, mid)
    # 再处理右边部分
    mergesort(arr, mid + 1, r)
    # 合并2个已经排好序的子数组
    merge(arr, l, mid, r)


def merge(arr, l, m, r):
    # 合并两个子数组
    tmp = []
    i = 0
    p1 = l
    p2 = m + 1
    while p1 <= m and p2 <= r:
        if arr[p1] < arr[p2]:
            tmp.append(arr[p1])
            p1 += 1
        else:
            tmp.append(arr[p2])
            p2 += 1
        i += 1
    # 处理p1剩下的元素
    while p1 <= m:
        tmp.append(arr[p1])
        p1 += 1
        i += 1
    # 处理p2剩下的元素
    while p2 <= r:
        tmp.append(arr[p2])
        p2 += 1
        i += 1

    for i in range(len(tmp)):
        arr[l + i] = tmp[i]


if __name__ == "__main__":
    arr = [1, 3, 5, 4, 2, 0]
    mergeSort(arr)
    assert arr == [0, 1, 2, 3, 4, 5]
