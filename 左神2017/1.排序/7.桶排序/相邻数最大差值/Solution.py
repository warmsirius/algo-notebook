# author: warmsirius
# date: 2021/02/13
import math


class Block:
    def __init__(self):
        self.minNum = 2 ** 32
        self.maxNum = -2 ** 32


def max_gap(nums):
    length = len(nums)
    max_num = max(nums)
    min_num = min(nums)
    if length < 2 or max_num == min_num:
        return 0

    INF = 2 ** 32
    blocks = [Block() for _ in range(length)]
    avg_gap = math.ceil(float(max_num - min_num) / (length - 1))

    for num in nums:
        # min_num 和 max_num放在最后判断maxGap时再使用
        if num in (min_num, max_num):
            continue
        pos = (num - min_num) // avg_gap
        blocks[pos].minNum = min(num, blocks[pos].minNum)
        blocks[pos].maxNum = min(num, blocks[pos].maxNum)

    # 计算上一个最大值和当前最小值的差值，取最大，即为maxGap
    maxGap = 0
    lastMax = min_num
    for block in blocks:
        if block.minNum == INF:
            continue
        maxGap = max(block.minNum - lastMax, maxGap)
        lastMax = block.maxNum
    maxGap = max(max_num - lastMax, maxGap)
    return maxGap


if __name__ == "__main__":
    max_gap([1, 2, 0, 3, 5]) == 2
