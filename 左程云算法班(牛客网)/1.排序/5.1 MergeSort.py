def mergeSort(arr):
    if arr == [] or len(arr) < 2:
        return
    mergesort(arr, 0, len(arr) - 1)


def mergesort(arr, l, r):
    if l == r:
        return
    mid = l + ((r - l) >> 1)
    mergesort(arr, l, mid)
    mergesort(arr, mid + 1, r)
    merge(arr, l, mid, r)


def merge(arr, l, m, r):
    tmp = []
    i = 0
    p1 = l
    p2 = m + 1
    while p1 <= m and p2 <= r:
        if arr[p1] < arr[p2]:
            tmp.append(arr[p1])
            p1 += 1
        else:
            tmp.append(arr[p2])
            p2 += 1
        i += 1

    while p1 <= m:
        tmp.append(arr[p1])
        p1 += 1
        i += 1
    while p2 <= r:
        tmp.append(arr[p2])
        p2 += 1
        i += 1

    for i in range(len(tmp)):
        arr[l + i] = tmp[i]


arr = [1, 3, 5, 4, 2, 0]
mergeSort(arr)
print(arr)
