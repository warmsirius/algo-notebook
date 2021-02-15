from enum import Enum


def hanoiProblem1(num, left, mid, right) -> int:
    """方法一: 递归思想求解汉诺塔"""
    if num < 1:
        return 0
    else:
        return process(num, left, mid, right, left, right)


def process(num, left, mid, right, _from, _to) -> int:
    """汉诺塔递归函数"""
    # 如果只有1个元素需要移动，同样也是递归终止条件
    if num == 1:
        # 从左/右->中、中->左/右
        if _from == mid or _to == mid:
            print(f"Move 1 from {_from} to {_to}")
            return 1
        # 从左->右、右->左
        else:
            print(f"Move 1 from {_from} to mid")
            print(f"Move 1 from mid to {_to}")
            return 2
    # 任意一次从 左/右 -> 中、中 -> 左、右
    if _from == mid or _to == mid:
        # 根据之前的分析，分为3步
        # another: 找到另一根柱子
        another = right if (_from == left or _to == left) else left
        # 第一步: 递归其余N-1的先给我放到另一个柱子上去
        part1 = process(num - 1, left, mid, right, _from, another)

        # 第二步: 当前这一个直接从 _from 移动到 _to，因为其中1个为mid
        part2 = 1
        print(f"Move 1 from  {_from} to {_to}")

        # 第三步: 递归将n-1个元素从 another移动到 _to
        part3 = process(num - 1, left, mid, right, another, _to)

        # 结束
        return part1 + part2 + part3
    # 任意一次从 左 -> 右、右 -> 左
    else:
        # 第一步: 递归其余N-1个先给我从左(_from)到右(_to)放过去
        part1 = process(num - 1, left, mid, right, _from, _to)

        # 第二步: 将第N层，从左(_from)到中
        part2 = 1
        print(f"Move {num} from {_from} to {mid}")

        # 第三步: 递归其余N-1层继续从右(_to)到左(_from)放过去
        part3 = process(num - 1, left, mid, right, _to, _from)

        # 第四步: 将第N层，从中到右(_to)
        part4 = 1
        print(f"Move {num} from {mid} to {_to}")

        # 第五步: 递归其余N-1层，从左(_from)到右(_to)
        part5 = process(num - 1, left, mid, right, _from, _to)
        return part1 + part2 + part3 + part4 + part5


class Action(Enum):
    No = "No"
    LToM = "LToM"
    MToL = "MToL"
    RToM = "RToM"
    MToR = "MToR"


def hanoiProblem2(num, left, mid, right) -> int:
    """用栈求解汉诺塔"""
    LS = [float("inf")]
    MS = [float("inf")]
    RS = [float("inf")]

    # 初始化 LS栈，依次从大到小压入
    for i in range(num, 0, -1):
        LS.append(i)

    # 初始化上一步移动记录为 No，这样不和任何移动起冲突
    record = [Action.No.name]

    step = 0
    # while 里面内部的移动，4个当中只有1个会执行，其余3个都不符合移动的原则
    while len(RS) != num + 1:
        # 1次移动: 从左到中
        step += fStackToStack(record, Action.MToL.name, Action.LToM.name, LS, MS, left, mid)
        # 1次移动: 从中到左
        step += fStackToStack(record, Action.LToM.name, Action.MToL.name, MS, LS, mid, left)
        # 1次移动: 从右到中
        step += fStackToStack(record, Action.MToR.name, Action.RToM.name, RS, MS, right, mid)
        # 1次移动: 从中到右
        step += fStackToStack(record, Action.RToM.name, Action.MToR.name, MS, RS, mid, right)
    return step


def fStackToStack(record, preNoAct, nowAct, fStack, tStack, _from, _to) -> int:
    """从一个栈移动到另1个栈"""
    if (record[0] != preNoAct) and (fStack[-1] < tStack[-1]):
        # 原则1: 不可大压小， Stack[-1] < tStack[-1]，否则不满足条件
        # 原则2: 相邻操作不可逆序，record[0] != preNoAct: preNoAct就是nowAct的逆序操作
        tStack.append(fStack.pop())
        print(f"Move {tStack[-1]} from {_from} to {_to}")
        # 更新上一步的操作
        record[0] = nowAct
        return 1
    else:
        return 0


if __name__ == "__main__":
    ret = hanoiProblem1(2, "left", "mid", "right")
    assert ret == 8

    ret = hanoiProblem2(2, "left", "mid", "right")
    assert ret == 8
