import random;


def randomQuickSort(arr):
    """随机快排"""
    if arr == [] or len(arr) < 2:
        return arr
    quickSort(arr, 0, len(arr) - 1)


def quickSort(arr, l, r):
    """快速排序主要流程"""
    if l < r:
        swap(arr, int(l + random.random() * (r - l + 1)), r)
        i, j = partition(arr, l, r)
        quickSort(arr, l, i - 1)
        quickSort(arr, j, r)


def partition(arr, l, r):
    """分割3个区域操作"""
    less = l - 1
    more = r
    while l < more:
        if arr[l] < arr[r]:
            less += 1
            swap(arr, less, l)
            l += 1
        elif arr[l] > arr[r]:
            swap(arr, more, l)
            more -= 1
        else:
            l += 1
    swap(arr, more, r)
    return less + 1, more


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


arr = [1, 4, 3, 2, 0, 9, 7, 6]
randomQuickSort(arr)
print(arr)
