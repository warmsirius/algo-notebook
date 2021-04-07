class Node:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None


def getMaxLength(head: Node, sum: int):
    sumMap = dict()
    sumMap[0] = 0
    return preOrder(head, sum, 0, 1, 0, sumMap)


def preOrder(head: Node, sum: int, preSum: int, level: int, maxLen: int, sumMap: dict):
    if head is None:
        return maxLen

    curSum = preSum + head.value
    if curSum not in sumMap:
        sumMap[curSum] = level
    if curSum - sum in sumMap:
        maxLen = max(level - sumMap.get(curSum - sum), maxLen)

    maxLen = preOrder(head.left, sum, curSum, level + 1, maxLen, sumMap)
    maxLen = preOrder(head.right, sum, curSum, level + 1, maxLen, sumMap)
    # 这里有点看不懂？为啥要这么做？
    if level == sumMap.get(curSum):
        del sumMap[curSum]
    return maxLen


node1 = Node(1)
node2 = Node(2)
node3 = Node(1)
node4 = Node(3)
node5 = Node(1)

node1.left = node2
node1.right = node4
node2.left = node3
node3.left = node5

print(getMaxLength(node1, 4))
