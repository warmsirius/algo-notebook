def insertionSort_1(arr):
    """插入排序"""
    # 方式一: 当前插入值，每步都进行值交换
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
            else:
                break


def insertionSort_2(arr):
    """插入排序"""
    # 方式2: 前面有序范围把大于需要插入的数往后移动一位，最后找到不大于插入的数就位置空，和插入的值进行交换
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j > -1 and arr[j] > key:
            swap(arr, j, j + 1)
            j -= 1
        arr[j + 1] = key


def swap(arr, i, j):
    """交换数组中i，j的值"""
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
