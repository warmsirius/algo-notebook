class Node(object):
    """节点"""
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self.header = None
        self.length = 0

    def check_index(self, index):
        """检查索引值是否合法"""
        if index <= 0 or index > self.length:
            while index <= 0 or index > self.length:
                print("你输入的下标不对，请重新输入需要删除的值的下标：")
                index = eval(input())
        return index

    def is_empty(self):
        """判断是否为空"""
        if self.header is None:
            return True
        else:
            return False

    def add(self, node):
        """头部插入"""
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node
        self.length += 1

    def append(self, node):
        """尾部插入"""
        currentNode = self.header
        if self.is_empty():
            self.add(node)
        else:
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = node
            self.length += 1

    def insert(self, node, index):
        """指定位置插入"""
        index = self.check_index(index)

        currentNode = self.header

        if index == 1:
            self.add(node)
        elif index == 2:
            node.next = self.header.next
            self.header.next = node
            self.length += 1
        else:
            for i in range(1, index - 1):
                currentNode = currentNode.next
            node.next = currentNode.next
            currentNode.next = node
            self.length += 1

    def travel(self):
        """遍历"""
        currentNode = self.header
        if self.length == 0:
            print("目前链表没有数据!")
        else:
            # end="": 不换行
            print("目前链表里的数据有:", end="")
            for i in range(self.length):
                print("%s " % currentNode.val, end=" ")
                currentNode = currentNode.next
            print("\n")

    def list_sort(self):
        """排序不用交换节点的位置，只需要交换节点上的数据值"""
        for i in range(0, self.length - 1):
            currentNode = self.header
            for j in range(0, self.length - i - 1):
                if currentNode.val > currentNode.next.val:
                    tmp = currentNode.val
                    currentNode.val = currentNode.next.val
                    currentNode.next.val = tmp
                currentNode = currentNode.next

    def delete(self, index):
        """按索引删除"""
        index = self.check_index(index)
        if index == 1:
            self.header = self.header.next
        elif index == 2:
            currentNode = self.header
            currentNode.next = currentNode.next.next
        else:
            currentNode = self.header
            for i in range(1, index - 1):
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
        self.length -= 1

    def isContain(self, x):
        contain = 0
        currentNode = self.header
        for i in range(self.length):
            if currentNode.val == x:
                print("%d在链表中%d处\n" % (x, i + 1))  # i+1是在正常人认为的位置处，程序员一般是从0开始算起
                contain = 1
            currentNode = currentNode.next
        if contain == 0:
            print("%d不在链表中" % x)

    def searchNodeByIndex(self, index):
        index = self.check_index(index)
        currentNode = self.header
        for i in range(index - 1):
            currentNode = currentNode.next
        return currentNode

    def alter(self, index, x):
        index = self.check_index(index)
        currentNode = self.header
        for i in range(index - 1):
            currentNode = currentNode.next
        currentNode.val = x


def main():
    # 创建一个节点对象
    node1 = Node(1)
    # 创建一个单链表对象
    single_link_list = SingleLinkList()  # 实例化

    print('''
          ******************************************************************
          **************************请选择相应的序号完成相应的操作***************
          ****************************************************************** 
          **         0、结束所有操作！！！！！！                             ***
          **         1、验证链表里面有没有值！                               ***
          **         2、从头部插入数值！                                    ***
          **         3、从尾部插入数值！                                    ***
          **         4、按指定位置插入数值！                                 ***
          **         5、删除操作！                                         ***
          **         6、查找一个节点是否在链表中！                            ***
          **         7、按下标查找节点处的数值！                              ***
          **         8、给链表排序！                                        ***
          **         9、修改！                                             ***
          ********************************************************************
          ''')
    while True:
        number = eval(input("——————输入下一步要进行的相应操作序号——————："))
        if (number == 1):
            print("正在验证链表里面有没有值：")
            single_link_list.travel()
            print("\n")

        if (number == 2):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在从头部插入数值：")
            node1 = Node(eval(input("输入要插入的值:")))  # 从头部插入数值
            single_link_list.add(node1)
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 3):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在尾部插入数值：")
            node2 = Node(eval(input("输入要插入的值:")))
            single_link_list.append(node2)
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 4):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在按指定位置插入数值：")
            node3 = Node(eval(input("输入插入的数：")))
            position = eval(input("输入要插入到的位置为："))
            single_link_list.insert(node3, position)
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 5):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在删除：")
            single_link_list.delete(eval(input("输入要删除哪个位置的数：")))
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 6):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在查找一个节点是否在链表中：")
            single_link_list.isContain(eval(input("输入要验证的数：")))

        if (number == 7):
            print("正在按下标查找节点处的数值：")
            node = single_link_list.searchNodeByIndex(eval(input("输入下标值：")))  # 查找某节点处的值
            print("这个位置的值为：%s" % node.element)

        if (number == 8):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在排序：")
            single_link_list.list_sort()
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 9):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在修改（这是在上面排序后的前提下修改。）：")
            index = eval(input("输入要修改的得位置："))  # 修改的下角标
            num = eval(input("输入要修改为的数："))  # 要修改成的那个数
            single_link_list.Alert(index, num)
            print("操作后链表的状态。")
            single_link_list.travel()  # 遍历一遍

        if number == 0:
            break


if __name__ == '__main__':
    main()
