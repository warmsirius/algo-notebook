def partition(arr, l, r, pivot):
    """数组进行分区"""
    # 根据 pivot值，将arr分为:
    # 1. 小于pivot值区域
    # 2. 等于pivot值区域
    # 3. 大于pivot值区域
    less = l - 1
    more = r
    while l < more:
        if arr[l] < pivot:
            less += 1
            swap(arr, less, l)
            l += 1
        elif arr[l] == pivot:
            l += 1
        else:
            more -= 1
            swap(arr, more, l)
    return arr


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


if __name__ == "__main__":
    arr = [1, 4, 5, 9, 8, 6, 2, 1, 3, 4]
    partition(arr, 0, len(arr), 5)
    assert arr == [1, 4, 4, 3, 1, 2, 5, 6, 8, 9]
