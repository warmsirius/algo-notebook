def radix_sort(arr, radix=10):
    """a为整数列表， radix为基数"""
    j = len(str(max(arr)))
    i = 0
    while i < j:
        # 初始化桶数组，不能使用 [[]]*radix，这样会共享[]的地址，造成数据重复
        bucket = [[] for _ in range(radix)]
        for x in arr:
            bucket[int(x / (10 ** i) % 10)].append(x)

        # 清空数组，重新压入数据
        arr.clear()
        for x in bucket:
            for y in x:
                arr.append(y)
        i += 1
    return arr


if __name__ == '__main__':
    assert radix_sort([78, 87, 98, 100]) == [78, 87, 98, 100]
