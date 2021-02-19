"""
最小栈解法:
    twoSum1: 第一种设计方案，2次遍历
    twoSum2: 第二种设计方案，空间换时间，1次遍历
"""


def twoSum1(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum2(nums, target):
    tmp = dict()
    for index, i in enumerate(nums):
        if target - i not in tmp:
            tmp[i] = index
        else:
            return [tmp[target - i], index]
