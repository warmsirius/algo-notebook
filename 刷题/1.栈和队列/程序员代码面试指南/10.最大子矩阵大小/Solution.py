# @author: warmsirius
# @date: 2021/02/17

def max_rec_size(map_in):
    if map_in == [] or len(map_in) == 0 or len(map_in[0]) == 0:
        return 0
    max_area = 0
    # 构造height数组
    height = [0 for _ in range(len(map_in[0]))]
    for i in range(len(map_in)):
        # 依次按照，第1行、第2行...进行切割
        for j in range(len(map_in[0])):
            height[j] = 0 if map_in[i][j] == 0 else height[j] + 1
        # 切割后求该行的最大子矩阵大小
        max_area = max(max_rec_from_bottom(height), max_area)
    return max_area


def max_rec_from_bottom(height):
    """计算height能生成的最大矩阵大小"""
    if height == [] or len(height) == 0:
        return 0
    max_area = 0
    stack = []
    for i in range(len(height)):
        # 维护单调栈的特性，压入元素小于栈顶且栈不为空
        while stack and height[i] <= height[stack[-1]]:
            # 右侧能扩展的最大值: i - 1
            j = stack.pop()
            # 左侧能扩展的最大值: k + 1
            # 如果栈为空，k+1=0，所以 k = -1
            k = -1 if len(stack) == 0 else stack[-1]
            # 计算当前的矩阵区域
            cur_area = (i - k - 1) * height[j]
            max_area = max(max_area, cur_area)
        stack.append(i)

    # 清算单调栈剩下的元素
    while stack:
        # 右侧能扩展的位置: len(height) - 1
        j = stack.pop()
        # 左侧能扩展的位置: k + 1
        # 如果栈为空，k+1=0，所以 k = -1
        k = -1 if len(stack) == 0 else stack[-1]
        # len(height) - 1 - (k + 1) + 1 = len(height) - k - 1
        cur_area = (len(height) - k - 1) * height[j]
        max_area = max(max_area, cur_area)
    return max_area


if __name__ == '__main__':
    assert max_rec_size([[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]) == 6
