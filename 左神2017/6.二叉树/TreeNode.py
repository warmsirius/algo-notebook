class TreeNode(object):
    """构造二叉树"""
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return str(self.data)
