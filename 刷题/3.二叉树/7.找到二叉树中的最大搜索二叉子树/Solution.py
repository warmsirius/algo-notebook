class Node:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None


import sys


class ReturnType(object):
    def __init__(self, maxBSTHead, maxBSTSize, min, max):
        self.maxBSTHead = maxBSTHead
        self.maxBSTSize = maxBSTSize
        self.min = min
        self.max = max


def process(X: Node):
    if X is None:
        return ReturnType(None, 0, sys.maxsize, -sys.maxsize - 1)
    lData = process(X.left)
    rData = process(X.right)

    min_val = min(X.value, min(lData.min, rData.min))
    max_val = max(X.value, max(lData.max, rData.max))
    maxBSTSize = max(lData.maxBSTSize, rData.maxBSTSize)
    maxBSTHead = lData.maxBSTHead if lData.maxBSTSize >= rData.maxBSTSize else rData.maxBSTHead
    if lData.maxBSTHead == X.left and rData.maxBSTHead == X.right and X.value > lData.max and X.value < rData.min:
        maxBSTSize = lData.maxBSTSize + rData.maxBSTSize + 1
        maxBSTHead = X
    return ReturnType(maxBSTHead, maxBSTSize, min_val, max_val)


def getMaxBST(head: Node):
    return process(head).maxBSTHead



