import random;


def randomQuickSort(arr):
    """随机快排"""
    if arr == [] or len(arr) < 2:
        return arr
    quick_sort(arr, 0, len(arr) - 1)


def partition(arr, l, r):
    """分区"""
    # l: 移动指针，循环停止条件 l >= more
    # r: 基准值，arr[r] 和 arr[l] 进行比较
    # less: 小于区域的指针，从l-1开始计算
    less = l - 1
    # more: 大于区域的指针，从r开始计算
    more = r
    while l < more:
        if arr[l] < arr[r]:
            # 当arr[l] < arr[r]时，less指针加1，l指针加1
            less += 1
            swap(arr, less, l)
            l += 1
        elif arr[l] == arr[r]:
            # 当arr[l] = arr[r]时，l指针+1，但是less指针不动
            l += 1
        else:
            # 当arr[l] > arr[r]时，和more前面的一位进行交换，然后指针均保持不动
            more -= 1
            swap(arr, more, l)
    # 最后再将最后1个元素，也就是基准值和more的值进行交换
    # 这样，等于的放在了一起，大于的放在了一起，小于的放在了一起
    swap(arr, r, more)
    return less + 1, more


def quick_sort(arr, l, r):
    if l < r:
        swap(arr, int(l + random.random() * (r - l + 1)), r)
        i, j = partition(arr, l, r)
        quick_sort(arr, l, i - 1)
        quick_sort(arr, j, r)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


if __name__ == "__main__":
    arr = [5, 3, 4, 1, 2, 0, 2, 1, 3]
    randomQuickSort(arr)
    assert arr == [0, 1, 1, 2, 2, 3, 3, 4, 5]

    arr = [1, 4, 3, 2, 0, 9, 7, 6]
    randomQuickSort(arr)
    assert arr == [0, 1, 2, 3, 4, 6, 7, 9]
