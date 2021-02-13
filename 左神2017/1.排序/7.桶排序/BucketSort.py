# author: warmsirius
# date: 2021/02/13
import math


def bucktetSort(numList):
    """桶排序函数"""
    if len(numList) <= 0:
        return numList

    maxNum = max(numList)
    minNum = min(numList)

    bucketLength = len(numList) - 1
    bucketSize = ((maxNum - minNum) / bucketLength)  # 根据桶的数量找到每个桶的取值范围
    buckets = [[] for i in range(bucketLength)]

    for i in range(len(numList)):  # 将各个数分配到各个桶
        # num_buckets_local界定范围.只要大于第n个桶,就是在第n+1个桶里.所以是向上取整.
        # 比如说 numList = [1,40,50,60,200].
        num_buckets_local = math.ceil((numList[i] - minNum) / bucketSize) - 1
        # 最小值是 == -1 的
        num_buckets_local = 0 if num_buckets_local <= 0 else num_buckets_local
        buckets[num_buckets_local].append(numList[i])

    # ---可删除---
    print('桶的取值范围是:', bucketSize)
    print('每个桶的藏的宝贝都是:', buckets)
    # ---可删除---

    for i in range(bucketLength):  # 桶内排序，可以使用各种排序方法
        buckets[i].sort()

    res = []
    for i in range(len(buckets)):  # 分别将各个桶内的数提出来，压入结果
        res.extend(buckets[i])
    return res


if __name__ == "__main__":
    numlist = [1, 50.76, 75, 150, 200, 321, 321, 32, 992]
    print(bucktetSort(numlist, 5), '\n' * 2)
