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


prefixSum = [0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2, 3, 4, 5]
res = 0
i = 0
j = 0
num = len(prefixSum)
for i in range(num):
    for j in range(i + 1, num):
        # 检查每一对下标看是否符合条件
        if prefixSum[i] < prefixSum[j]:
            res = max(j - i, res)
            print(res)
print(res)


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for i in preorder.split(","):
            import pdb; pdb.set_trace()
            if i == "#" and len(stack) > 3 and stack[-1] == "#" and stack[-2] != "#":
                stack.pop()
                stack.pop()
                stack.append("#")
            else:
                stack.append(i)
        return len(stack) == 1 and stack[0]== "#"


print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))