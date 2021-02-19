class Node(object):
    """节点"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self.header = None
        self.length = 0

    def is_empty(self):
        """判断单链表是否为空"""
        return True if self.header is None else False

    def add(self, node: Node):
        """头部插入节点"""
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node
        self.length += 1

    def append(self, node: Node):
        """尾部插入节点"""
        cur_node = self.header
        if self.is_empty():
            self.add(node)
        else:
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node
            node.next = Node
        self.length += 1

    def insert(self, index: int, node: Node):
        """指定位置插入节点"""
        cur_node = self.header
        index = self.check_index(index)

        if index == 1:
            self.add(node)
        elif index == 2:
            node.next = self.header.next
            self.header.next = node
        else:
            for i in range(1, index - 1):
                cur_node = cur_node.next
            node.next = cur_node.next
            cur_node.next = node
        self.length += 1

    def travel(self):
        """遍历链表"""
        cur_node = self.header
        if self.length == 0:
            print("当前链表没有数据!")
        else:
            while cur_node is not None:
                print(cur_node.value)
                cur_node = cur_node.next

    def delete(self, index: int):
        """按照索引删除节点"""
        index = self.check_index(index)

        cur_node = self.header
        if index == 1:
            self.header = self.header.next
            cur_node.next = None
        elif index == 2:
            cur_node.next = cur_node.next.next
        else:
            for i in range(1, index - 1):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
        self.length -= 1

    def is_contain(self, num):
        """查找是否包含某元素，并返回下标"""
        cur_node = self.header
        index = 1
        while cur_node is not None or cur_node.value != num:
            index += 1
            cur_node = cur_node.next

        if cur_node is None:
            print("不包含该元素")
            return None
        if cur_node.value == num:
            print(f"下标是: {index}")
            return index

    def search_node_by_index(self, index: int):
        """根据下标找节点"""
        index = self.check_index(index)
        cur_node = self.header
        for i in range(index - 1):
            cur_node = cur_node.next
        return cur_node

    def alter(self, index, num):
        """根据下标修改节点值"""
        index = self.check_index(index)
        cur_node = self.header
        for i in range(index - 1):
            cur_node = cur_node.next
        cur_node.value = num
        return cur_node

    def list_sort(self):
        """排序链表"""
        # 不用交换节点的位置，只需要交换节点上的数据值
        # 排序方式: 冒泡排序
        for i in range(self.length - 1):
            cur_node = self.header
            for j in range(self.length - i - 1):
                if cur_node.value > cur_node.next.value:
                    temp = cur_node.value
                    cur_node.value = cur_node.next.value
                    cur_node.next.value = temp

                cur_node = cur_node.next

    def check_index(self, index):
        if index > self.length or index <= 0:
            while index > self.length or index <= 0:
                print("你输入的下标不对，请重新输入需要删除的值的下标:")
                index = eval(input())
        return index


def main():
    # 创建一个节点对象
    node1 = Node(1)
    # 创建一个单链表对象
    single_link_list = SingleLinkList()  # 实例化

    print('''
          **********************************************************************************************************************
          **********************************************请选择相应的序号完成相应的操作********************************************
          **********************************************************************************************************************   
          **         0、结束所有操作！！！！！！                                                                               ***
          **         1、验证链表里面有没有值！                                                                                 ***
          **         2、从头部插入数值！                                                                                       ***
          **         3、从尾部插入数值！                                                                                       ***
          **         4、按指定位置插入数值！                                                                                   ***
          **         5、删除操作！                                                                                            ***
          **         6、查找一个节点是否在链表中！                                                                             ***
          **         7、按下标查找节点处的数值！                                                                               ***
          **         8、给链表排序！                                                                                          ***
          **         9、修改！                                                                                                ***
          **********************************************************************************************************************
          ''')
    while True:
        number = eval(input("——————输入下一步要进行的相应操作序号——————："))
        if number == 1:
            print("正在验证链表里面有没有值：")
            single_link_list.travel()
            print("\n")
        if number == 2:
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在从头部插入数值：")
            node1 = Node(eval(input("输入要插入的值:")))  # 从头部插入数值
            single_link_list.add(node1)
            print("操作后链表的状态。")
            single_link_list.travel()

        if number == 3:
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在尾部插入数值：")
            node2 = Node(eval(input("输入要插入的值:")))
            single_link_list.append(node2)
            print("操作后链表的状态。")
            single_link_list.travel()

        if number == 4:
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在按指定位置插入数值：")
            node3 = Node(eval(input("输入插入的数：")))
            position = eval(input("输入要插入到的位置为："))
            single_link_list.insert(node3, position)
            print("操作后链表的状态。")
            single_link_list.travel()

        if number == 5:
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在删除：")
            single_link_list.delete(eval(input("输入要删除哪个位置的数：")))
            print("操作后链表的状态。")
            single_link_list.travel()

        if number == 6:
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在查找一个节点是否在链表中：")
            single_link_list.is_contain(eval(input("输入要验证的数：")))

        if number == 7:
            print("正在按下标查找节点处的数值...")
            node = single_link_list.search_node_by_index(eval(input("输入下标值：")))  # 查找某节点处的值
            print("这个位置的值为：%s" % node.value)

        if number == 8:
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在排序...")
            single_link_list.list_sort()
            print("操作后链表的状态。")
            single_link_list.travel()

        if number == 9:
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在修改（这是在上面排序后的前提下修改。）...")
            index = eval(input("输入要修改的得位置："))  # 修改的下角标
            num = eval(input("输入要修改为的数："))  # 要修改成的那个数
            single_link_list.alter(index, num)
            print("操作后链表的状态。")
            single_link_list.travel()  # 遍历一遍

        if number == 0:
            break


if __name__ == '__main__':
    main()
