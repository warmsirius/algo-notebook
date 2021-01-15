from enum import Enum


def hanoiProblem1(num, left, mid, right) -> int:
    """
    用递归求解汉诺塔
    :param num:
    :param left:
    :param mid:
    :param right:
    :return:
    """
    if num < 1:
        return 0
    else:
        return process(num, left, mid, right, left, right)


def process(num, left, mid, right, _from, _to) -> int:
    if num == 1:
        if _from == mid or _to == mid:
            print(f"Move 1 from {_from} to {_to}")
            return 1
        else:
            print(f"Move 1 from {_from} to mid")
            print(f"Move 1 from mid to {_to}")
            return 2

    if _from == mid or _to == mid:
        another = right if (_from == left or _to == left) else left
        part1 = process(num - 1, left, mid, right, _from, another)
        part2 = 1
        print(f"Move 1 from  {_from} to {_to}")
        part3 = process(num - 1, left, mid, right, another, _to)
        return part1 + part2 + part3
    else:
        part1 = process(num - 1, left, mid, right, _from, _to)
        part2 = 1
        print(f"Move {num} from {_from} to {mid}")
        part3 = process(num - 1, left, mid, right, _to, _from)
        part4 = 1
        print(f"Move {num} from {mid} to {_to}")
        part5 = process(num - 1, left, mid, right, _from, _to)
        return part1 + part2 + part3 + part4 + part5


class Action(Enum):
    No = "No"
    LToM = "LToM"
    MToL = "MToL"
    RToM = "RToM"
    MToR = "MToR"


def hanoiProblem2(num, left, mid, right) -> int:
    """
    用栈求解汉诺塔
    :param num:
    :param left:
    :param mid:
    :param right:
    :return:
    """
    LS = [float("inf")]
    MS = [float("inf")]
    RS = [float("inf")]

    for i in range(num, 0, -1):
        LS.append(i)
    record = [Action.No.name]
    step = 0

    while len(RS) != num + 1:
        step += fStackToStack(record, Action.MToL.name, Action.LToM.name, LS, MS, left, mid)
        step += fStackToStack(record, Action.LToM.name, Action.MToL.name, MS, LS, mid, left)
        step += fStackToStack(record, Action.MToR.name, Action.RToM.name, RS, MS, right, mid)
        step += fStackToStack(record, Action.RToM.name, Action.MToR.name, MS, RS, mid, right)
    return step


def fStackToStack(record, preNoAct, nowAct, fStack, tStack, _from, _to) -> int:
    """
    从一个栈移动到另1个栈
    :param record:
    :param preNoAct:
    :param nowAct:
    :param fStack:
    :param tStack:
    :param _from:
    :param _to:
    :return:
    """
    if (record[0] != preNoAct) and (fStack[-1] < tStack[-1]):
        # record[0]: 代表上一步的动作
        # record[0] != preNoAct: 代表nowAct和上一次操作为非逆序操作
        # fStack[-1] < tStack[-1]: 代表要移动的栈顶 < 另一方栈顶，否则不满足条件
        tStack.append(fStack.pop())
        print(f"Move {tStack[-1]} from {_from} to {_to}")
        record[0] = nowAct
        return 1
    else:
        return 0


if __name__ == "__main__":
    ret = hanoiProblem1(2, "left", "mid", "right")
    assert ret == 8

    ret = hanoiProblem2(2, "left", "mid", "right")
    assert ret == 8
