class TwoStacksQueue(object):
    """2个栈组成的队列"""
    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def add(self, v):
        """向队列添加1个元素"""
        self.stackPush.append(v)

    def poll(self):
        """删除队列第1个元素"""
        if (not self.stackPush) and (not self.stackPop):
            raise Exception("Queue is empty!")
        elif not self.stackPop():
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
            return self.stackPop.pop()
        else:
            return self.stackPop.pop()

    def peek(self):
        """获取队列头部元素"""
        if (not self.stackPush) and (not self.stackPop):
            raise Exception("Queue is empty!")
        elif not self.stackPop():
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
            return self.stackPop[-1]
        else:
            return self.stackPop[-1]
