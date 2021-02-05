class TwoStackQueue(object):
    def __init__(self):
        # 维护2个栈: 1个数据压入栈，1个数据弹出栈
        self.stackPush = []
        self.stackPop = []

    def add(self, new_num):
        # stackPop压入1个值
        self.stackPush.append(new_num)

    def pull(self):
        # stackPop弹出1个值
        self.push_to_pop()
        if not self.stackPop:
            return None
        else:
            return self.stackPop.pop()

    def push_to_pop(self):
        # 当stackPop不为空的时候，将stackPush全部压入到stackPop
        if self.stackPop:
            pass
        else:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())

    def peek(self):
        self.push_to_pop()
        if not self.stackPop:
            return None
        else:
            return self.stackPop[-1]


if __name__ == "__main__":
    two_stack_queue = TwoStackQueue()
    two_stack_queue.add(1)
    two_stack_queue.add(2)
    two_stack_queue.add(3)
    assert two_stack_queue.peek() == 1
    assert two_stack_queue.pull() == 1
    assert two_stack_queue.peek() == 2
    assert two_stack_queue.pull() == 2
    assert two_stack_queue.pull() == 3
    assert two_stack_queue.pull() is None
    assert two_stack_queue.peek() is None
