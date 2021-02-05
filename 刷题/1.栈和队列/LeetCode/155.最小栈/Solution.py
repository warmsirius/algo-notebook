"""
最小栈解法:
    MinStack1: 第一种设计方案，stackData每压入1个元素，都压入该次对应的最小元素到stackMin
    MinStack2: 第二种设计方案，stackData每压入1个元素，如果压入元素是压入后最小的元素，才压入到stackMin
"""


class MinStack1(object):
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, x: int) -> None:
        if not self.stackMin:
            self.stackMin.append(x)
        elif x <= self.getMin():
            self.stackMin.append(x)
        else:
            self.stackMin.append(self.getMin())

        self.stackData.append(x)

    def pop(self) -> None:
        if not self.stackData:
            raise Exception("Your stack is empty.")

        value = self.stackData.pop()
        self.stackMin.pop()

        return value

    def top(self) -> int:
        if not self.stackData:
            raise Exception("Your stack is empty.")
        return self.stackData[-1]

    def getMin(self) -> int:
        if not self.stackMin:
            raise Exception("Your stack is empty.")
        return self.stackMin[-1]


class MinStack2(object):
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, x: int) -> None:
        if not self.stackMin:
            self.stackMin.append(x)
        elif x <= self.getMin():
            self.stackMin.append(x)

        self.stackData.append(x)

    def pop(self) -> None:
        if not self.stackData:
            raise Exception("Your stack is empty.")

        value = self.stackData.pop()
        if value == self.getMin():
            self.stackMin.pop()
        return value

    def top(self) -> int:
        if not self.stackData:
            raise Exception("Your stack is empty.")
        return self.stackData[-1]

    def getMin(self) -> int:
        if not self.stackMin:
            raise Exception("Your stack is empty.")
        return self.stackMin[-1]
