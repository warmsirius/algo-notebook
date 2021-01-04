"""
数组如果有序后，相邻数之间最大差值

原数组: [3, 4, 0, 9, 10]

排序后: [0, 3, 4, 9, 10]

0 和 10之间: 10

要求: 时间复杂度: O(N)
"""


def maxGap(nums):
    if nums == [] or len(nums) < 2:
        return nums
    length = len(nums)
    min = 0
    max = 0
    for i in range(nums):
        min = min(min, nums[i])
        max = max(max, nums[i])

    if min == max:
        return 0
    hasNum = []
    maxs = []
    mins = []

    for i in range(length):
        bid = bucket(nums[i], len, min, max)
        mins[bid] = min(mins[bid], nums[i]) if hasNum[bid] else nums[i]
        maxs[bid] = max(maxs[bid], nums[i]) if hasNum[bid] else nums[i]
        hasNum[bid] = True

    res = 0
    lastMax = maxs[0]
    for i in range(1, length+1):
        if hasNum[i]:
            res = max(res, mins[i] - lastMax)
            lastMax = max[i]
    return res


def bucket(num, len, min, max):
    return int((num - min) * len / (max - min))
