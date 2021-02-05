def small_sum(arr):
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
        if arr[p1] < arr[p2]:
            tmp.append(arr[p1])
            res += (r - p2 + 1) * arr[p1]
            p1 += 1
        else:
            tmp.append(arr[p2])
            p2 += 1
        i += 1
    # 处理p1剩下的元素，一般都是最大的元素了
    # 之前res已经计算过了，无序再计算
    while p1 <= m:
        tmp.append(arr[p1])
        p1 += 1
        i += 1
    # 处理p2剩下的元素，一般都是最大的元素了
    # 之前res已经计算过了，无序再计算
    # p1 和 p2元素是不可能同时留下的
    while p2 <= r:
        tmp.append(arr[p2])
        p2 += 1
        i += 1
    for i in range(len(tmp)):
        arr[l + i] = tmp[i]
    return res


if __name__ == "__main__":
    arr = [3, 5, 1, 4, 6]
    assert small_sum(arr) == 20
