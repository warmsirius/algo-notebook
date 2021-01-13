class MyStack1(object):
    """方案一代码"""

    def __init__(self):
        self._stackData = []
        self._stackMin = []

    def push(self, newNum):
        if not self._stackMin:
            self._stackMin.append(newNum)
        elif self.getMin() >= newNum:
            self._stackMin.append(newNum)
        else:
            self._stackMin.append(self.getMin())

        self._stackData.append(newNum)

    def pop(self) -> int:
        if self._stackData:
            self._stackMin.pop()
            return self._stackData.pop()
        else:
            raise Exception("Your stack is empty!")

    def getMin(self) -> int:
        if self._stackMin:
            return self._stackMin[-1]
        else:
            return Exception("Your stack is empty!")


class MyStack2(object):
    """方案二代码"""

    def __init__(self):
        self._stackData = []
        self._stackMin = []

    def push(self, newNum):
        if not self._stackMin:
            self._stackMin.append(newNum)
        elif self.getMin() >= newNum:
            self._stackMin.append(newNum)
        else:
            pass

        self._stackData.append(newNum)

    def pop(self) -> int:
        if self._stackData:
            v = self._stackData.pop()
            if v == self.getMin():
                self._stackMin.pop()
            return v
        else:
            raise Exception("Your stack is empty!")

    def getMin(self) -> int:
        if self._stackMin:
            return self._stackMin[-1]
        else:
            return Exception("Your stack is empty!")


if __name__ == "__main__":
    # 测试MyStack1
    stack1 = MyStack1()
    stack1.push(5)
    stack1.push(4)
    stack1.push(3)
    stack1.push(2)
    stack1.push(1)
    assert stack1.getMin() == 1
    assert stack1.pop() == 1
    # 测试MyStack2
    stack2 = MyStack2()
    stack2.push(5)
    stack2.push(4)
    stack2.push(3)
    stack2.push(2)
    stack2.push(1)
    assert stack2.getMin() == 1
    assert stack2.pop() == 1
