# @author: warmsirius
# @date: 2021/02/17


class Record(object):
    def __init__(self, value):
        self.value = value
        self.times = 1


def get_visible_num(arr):
    """获取可见山峰的数量"""
    if arr == [] or len(arr) < 2:
        return 0
    size = len(arr)
    max_index = 0
    # 先在环中找到其中1个最大值的位置，哪一个都行
    for i in range(size):
        max_index = i if arr[max_index] < arr[i] else max_index

    # 先把(最大值, 1)这个记录放入 stack中
    stack = []
    stack.append(Record(arr[max_index]))

    # 从最大位置的下一个位置开始沿next方向遍历
    index = next_index(max_index, size)

    # 用 小找大 的方式统计所有可见山峰对
    res = 0
    while index != max_index:
        # 当前数字进栈，不能破坏第一维数组从栈顶到栈底依次那个变大
        # 如果破坏了，就一次弹出栈顶记录，并计算山峰对数量
        while stack[-1].value < arr[index]:
            k = stack.pop().times
            # 弹出记录记为(X, K)，如果K==1，产生2对；如果K>1，产生 2*K+C(2, K)对
            res += get_internal_sum(k) + 2 * k
        if stack[-1].value == arr[index]:
            stack[-1].times += 1
        else:
            stack.append(Record(arr[index]))
        index = next_index(index, size)

    # 清算阶段开始
    # 清算阶段的第 1 小阶段
    while len(stack) > 2:
        times = stack.pop().times
        res += get_internal_sum(times) + 2 * times
    # 清算阶段的第 2 小阶段
    if len(stack) == 2:
        times = stack.pop().times
        res += get_internal_sum(times) + (times if stack[-1].times == 1 else 2 * times)
    # 清算阶段的第 3 小阶段
    res += get_internal_sum(stack.pop().times)
    return res


def get_internal_sum(k):
    """如果k==1，返回0；如果k > 1，返回C(2,K)"""
    return 0 if k == 1 else int((k * (k - 1) / 2))


def next_index(i, size):
    """环形数组中当前位置为i，数组长度为size，返回i的下一个位置"""
    return i + 1 if i < size - 1 else 0


if __name__ == '__main__':
    get_visible_num([4, 4, 2, 4, 5, 3, 4, 5, 2, 3, 5]) == 22
