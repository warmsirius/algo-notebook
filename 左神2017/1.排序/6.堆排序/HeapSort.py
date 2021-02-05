def HeapSort(arr):
    if arr == [] or len(arr) < 2:
        return;
    for i in range(len(arr)):
        heapInsert(arr, i)

    size = len(arr) - 1
    swap(arr, 0, size)

    while size > 0:
        heapify(arr, 0, size)
        size -= 1
        swap(arr, 0, size)


def heapInsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:
        swap(arr, index, int((index - 1) / 2))
        index = int((index - 1) / 2)


def heapify(arr, index, size):
    left = 2 * index + 1
    while left < size:
        largest = left + 1 if left + 1 < size and arr[left + 1] > arr[left] else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break

        swap(arr, largest, index)
        index = largest
        left = 2 * index + 1


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


arr = [6, 4, 2, 3, 1]
HeapSort(arr)
print(arr)
