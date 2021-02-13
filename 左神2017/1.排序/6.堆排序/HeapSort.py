# author: warmsirius
# date: 2021/02/13


def heap_sort(arr):
    """堆排序主函数"""
    if arr == [] or len(arr) < 2:
        return

    # 先将数组转换为大顶堆
    for i in range(len(arr)):
        heap_insert(arr, i)

    # 将最大值和最后1个元素进行交换
    size = len(arr) - 1
    swap(arr, 0, size)

    # 不断调整改变后的数组，保持大顶堆性质
    while size > 0:
        heapify(arr, 0, size)
        # 堆的缩小操作
        size -= 1
        swap(arr, 0, size)


def heapify(arr, index, size):
    """重新调整堆，使其剩下的依然保持大根堆"""
    left = 2 * index + 1
    while left < size:
        largest = left + 1 if (left + 1 < size and arr[left + 1] > arr[left]) else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        swap(arr, largest, index)
        index = largest
        left = 2 * index + 1


def heap_insert(arr, index):
    """将待排序序列构造成一个大顶堆"""
    while arr[index] > arr[int((index - 1) / 2)]:
        swap(arr, index, int((index - 1) / 2))
        index = int((index - 1) / 2)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


if __name__ == "__main__":
    arr = [6, 4, 2, 3, 1]
    heap_sort(arr)
    assert arr == [1, 2, 3, 4, 6]
