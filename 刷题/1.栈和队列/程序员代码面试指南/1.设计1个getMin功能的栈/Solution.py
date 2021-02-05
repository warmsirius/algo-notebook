class MyStack1(object):
    """方案一: 每一步都压入，每一步都弹出"""
    def __init__(self):
        # 维护2个栈，1个数据栈，1个最小值栈
        self._stackData = []
        self._stackMin = []

    def push(self, newNum):
        # 每一步都压入当前栈最小值
        # 比较newNum 和 当前栈最小值，压入较小的那个值
        if not self._stackMin:
            self._stackMin.append(newNum)
        elif self.getMin() >= newNum:
            self._stackMin.append(newNum)
        else:
            self._stackMin.append(self.getMin())

        self._stackData.append(newNum)

    def pop(self) -> int:
        # 每一步都弹出栈的最小值
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
    """方案二: 每一步只压入不大于当前栈的值，每一步弹出也只弹出不大于当前栈的值"""
    def __init__(self):
        # 维护2个栈，1个数据栈，1个最小值栈
        self._stackData = []
        self._stackMin = []

    def push(self, newNum):
        # newNum小于或等于栈当前最小值，压入
        if not self._stackMin:
            self._stackMin.append(newNum)
        elif self.getMin() >= newNum:
            self._stackMin.append(newNum)
        else:
            pass

        self._stackData.append(newNum)

    def pop(self) -> int:
        # newNum小于或等于栈当前最小值，弹出
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
