from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            swap(nums, i, nums[i] - 1)

    ans = []
    for i in range(n):
        if nums[i] != i + 1:
            ans.append(i + 1)
    return ans


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


if __name__ == "__main__":
    assert findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
