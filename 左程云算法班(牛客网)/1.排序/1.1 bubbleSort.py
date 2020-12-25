def bubbleSort(arr):
    """冒泡排序"""
    # 方式1: (外层索引从末尾开始取)外层索引 i 依次递减，内层索引递增 i
    n = len(arr)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


def bubbleSort(arr):
    """冒泡排序"""
    # 方式2: (外层索引从0开始取)外层索引 i 依次递增，内层索引递增到 arr.length - i - 2
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


def swap(arr, i, j):
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]
