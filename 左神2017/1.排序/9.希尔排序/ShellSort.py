# @author: warmsirius
# @date: 2021/02/15

def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            j = i
            while (j - gap) >= 0:
                if arr[j] < arr[j - gap]:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap = gap // 2
    return arr


if __name__ == '__main__':
    assert shell_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93]
