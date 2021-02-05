def reverse_pair(arr):
    """获取数组的逆序对"""
    if arr == [] or len(arr) < 2:
        return 0
    return merge_sort(arr, 0, len(arr) - 1)


def merge_sort(arr, l, r):
    if l == r:
        return 0
    mid = l + ((r - l) >> 1)
    return merge_sort(arr, l, mid) + merge_sort(arr, mid + 1, r) + merge(arr, l, mid, r)


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
            # 计算逆序对，p1..m位置的元素都大于 p2
            res += (m - p1 + 1)
            tmp.append(arr[p2])
            p2 += 1
        i += 1
    # 处理p1中没处理完的元素
    # 但是逆序对之前已经计算完了
    while p1 <= m:
        tmp.append(arr[p1])
        p1 += 1
        i += 1
    # 处理p2中没处理完的元素
    # 但是逆序对之前已经计算`完了
    while p2 <= r:
        tmp.append(arr[p2])
        p2 += 1
        i += 1

    for i in range(len(tmp)):
        arr[l + i] = tmp[i]
    return res


if __name__ == "__main__":
    arr = [1, 4, 3, 6]
    reverse_pair(arr) == 1
