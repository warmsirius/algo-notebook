class Node(object):
    def __init__(self, data):
        self.right = None
        self.left = None
        self.value = data


def getMaxTree(arr):
    """数组构造最大根二叉树"""
    import pdb; pdb.set_trace()
    nArr = [0] * len(arr)
    for i in range(len(arr)):
        nArr[i] = Node(arr[i])

    stack = []
    lBigMap = dict()
    rBigMap = dict()

    for i in range(len(arr)):
        curNode = nArr[i]
        while stack and stack[-1].value < curNode.value:
            popStackSetMap(stack, lBigMap)
        stack.append(curNode)

        while stack:
            popStackSetMap(stack, lBigMap)

        for i in range(len(arr) - 1, -1, -1):
            curNode = nArr[i]
            while stack and stack[-1].value < curNode.value:
                popStackSetMap(stack, rBigMap)
        while stack:
            popStackSetMap(stack, rBigMap)

        head = None
        for i in range(len(arr)):
            curNode = nArr[i]
            left = lBigMap.get(curNode)
            right = rBigMap.get(curNode)
            if (left is None) and (right is None):
                head = curNode
            elif left is None:
                if right.left is None:
                    right.left = curNode
                else:
                    right.right = curNode
            elif right is None:
                if left.left is None:
                    left.left = curNode
                else:
                    left.right = curNode
            else:
                parent = left if left.value < right.value else right
                if parent.left is None:
                    parent.left = curNode
                else:
                    parent.right = curNode
        return head


def popStackSetMap(stack, map):
    popNode = stack.pop()
    if stack:
        map[popNode] = stack[-1]
    else:
        map[popNode] = Node


if __name__ == "__main__":
    print(getMaxTree([3, 4, 6, 1, 2]))
