class SortStackByStack(object):
    """用1个栈实现另1个栈的排序"""
    def __init__(self, stack):
        self.stack = stack
        # _help: 从大到小保存stack中的值
        self._help = []

        while self.stack:
            cur_value = self.stack.pop()
            while self._help and cur_value > self._help[-1]:
                self.stack.append(self._help.pop())
            self._help.append(cur_value)
        # _help: 依次弹出，从小到大
        while self._help:
            self.stack.append(self._help.pop())


if __name__ == "__main__":
    stack = [4, 3, 1, 2, 1, 0]
    sort_stack_by_stack = SortStackByStack(stack)
    assert stack == [0, 1, 1, 2, 3, 4]
