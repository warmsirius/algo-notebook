def selectionSort_01(arr):
    """选择排序"""
    # 思路1: 每次选择出未排序范围最小的值
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            minIndex = j if arr[j] < arr[minIndex] else minIndex

        swap(arr, i, minIndex)


def selectionSort_02(arr):
    """选择排序"""
    # 思路2: 每次选择出未排序范围最大的值
    for i in range(len(arr) - 1, -1, -1):
        maxIndex = i
        for j in range(i):
            maxIndex = j if arr[j] > arr[maxIndex] else maxIndex
        swap(arr, i, maxIndex)


def swap(arr, i, j):
    """交换数组中i，j的值"""
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
