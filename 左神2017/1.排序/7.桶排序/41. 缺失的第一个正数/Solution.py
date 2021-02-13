from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    size = len(nums)
    for i in range(size):
        # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
        while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
            swap(nums, i, nums[i] - 1)

    for i in range(size):
        if i + 1 != nums[i]:
            return i + 1

    return size + 1


def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]
