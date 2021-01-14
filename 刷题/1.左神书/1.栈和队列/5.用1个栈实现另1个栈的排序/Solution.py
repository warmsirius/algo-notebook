class SortStackByStack(object):
    """用1个栈实现另1个栈的排序"""
    def __init__(self, stack):
        self.stack = stack
        self.help = []
        while self.stack:
            cur = self.stack.pop()
            while self.help and (help[-1] > cur):
                self.stack.append(self.help.pop())
            self.help.append(cur)
        while self.help:
            self.stack.append(self.help.pop())
