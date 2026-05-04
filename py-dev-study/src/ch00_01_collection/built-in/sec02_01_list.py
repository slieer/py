# -*- coding: utf-8 -*-

from collections import deque

"""
Created on 2010-7-3
@author: me
#filename: collection_list

list 官方名称：列表 (List),　动态数组, 可以做为队列，堆栈使用
print语句的结尾使用了一个 逗号 来消除每个print语句自动打印的换行符。

列表(List)：
python中最基本的数据结构，每一个元素被分配一个需要——元素的位置，亦称“索引”，首个索引为0，第二个为1，后面依此类推。
python包含六种内建的序列类型：列表、元组、字符串、Unicode字符串、buffer对象和xrange对象。
列表可变（可以进行修改），元组和字符串不可变（一旦创建了就是固定的）。
序列的两个主要特点是索引操作符和切片操作符。

为什么不称为“数组” (Array)？
虽然列表在底层实现上类似于动态数组，但在 Python 中，“数组”通常指 array 模块中的 array.array 或 NumPy 库中的 numpy.ndarray，它们要求元素类型一致且更侧重于数值计算。
Python 的 list 可以容纳不同类型的元素（如字符串、整数、对象等），因此不严格等同于传统意义上的“数组”。

为什么不是“序列” (Sequence)？
“序列”是一个更广泛的抽象概念或协议。
列表 (list)、元组 (tuple)、字符串 (str) 都属于序列类型。
所以，可以说列表是一种序列，但用 [] 创建的具体对象叫列表。

"""


class BaseListTest:
    def __init__(self):
        self.shoplist = ["apple", "mango", "carrot", "banana"]
        # Indexing or 'Subscription' operation
        print(
            "Item 0,1,2,3 is: %s, %s, %s, %s"
            % (self.shoplist[0], self.shoplist[1], self.shoplist[2], self.shoplist[3])
        )
        print("Item -1 is", self.shoplist[-1])  # 倒数第一个
        print("Item -2 is", self.shoplist[-2])  # 倒数第二个

        # Slicing on a list
        print(
            "Item 1 to 3 is", self.shoplist[1:3]
        )  # 取下标为1，下标2的两个元素。开始下标为0。
        print("Item 2 to end is", self.shoplist[2:])  # 取下标为2,到结尾的所有元素。
        print(
            "Item 1 to -1 is", self.shoplist[1:-1]
        )  # 取从下标为1的元素，及后面元素，不含最后一个。就是取除去序列两端的所有元素。
        print("Item start to end is", self.shoplist[:])  # 所有元素

        # Slicing on a string
        name = "swaroop"
        print("characters 1 to 3 is", name[1:3])
        print("characters 2 to end is", name[2:])
        print("characters 1 to -1 is", name[1:-1])
        print("characters start to end is", name[:])

        atuple = (2, 3, "老子")
        alist = list(atuple)
        alist[0] = 0
        btuple = tuple(alist)

        # 去掉重复内容，所以是 1,2,3,4,6
        aset = set([1, 2, 3, 2, 4, 6])
        # 建立一个集合的方式，是使用set()函数，函数的参数可以是列表，或者元祖，反正是一串儿的都可以
        # 集合也是可以变成列表的，利用 list() 函数。
        blist = list(aset)


class ListTest:
    shoplist = ["apple", "mango", "carrot", "banana"]

    def get(self):
        """'get 1, -1"""
        print("get  element ,index is 1", ListTest.shoplist[1])
        print("get  element ,index is -1", ListTest.shoplist[-1])

        # 　获取
        sub = ListTest.shoplist[-1:]  # 片段操作符，用于子list的提取
        print("sub[-1]:", sub)

        sub = ListTest.shoplist[0:1]  # 片段操作符，用于子list的提取
        print("sub[1]:", sub)

    def _len(self):
        print("I have", len(ListTest.shoplist), " items to purchase.")

    def _list(self):
        print("These items are:", end=" ")  # Notice the comma at end of the line
        for item in ListTest.shoplist:
            print(item, end=" ")

    def append(self):
        print("\nI also have to buy rice.")
        ListTest.shoplist.append("rice")
        print("My shopping list is now", ListTest.shoplist)

        ListTest.shoplist = ListTest.shoplist + [1, 2] + [3, 4]
        print(ListTest.shoplist)

    def append1(self):
        ListTest.shoplist[0:0] = ["sample value"]
        print(ListTest.shoplist)

        ListTest.shoplist[0:1] = ["sample value"]
        print(ListTest.shoplist)

    def _del(self):
        del ListTest.shoplist[0]
        print(ListTest.shoplist)


class StackTest:
    def __init__(
        self, arrayOjb=[]
    ):  # class StackTest(object): def __new__(self, arrayOjb=[]):   出错？？？？
        print("init stack test...")
        self.array = arrayOjb

    def enterStack(self, obj):
        self.array.append(obj)

    def readStactTop(self):
        return self.array[len(self.array) - 1]

    def popStactTopElement(self):
        return self.array.pop()


class QueueTest:
    def __init__(self, array):
        self.deque = deque(array)

    def read(self):
        deque.popleft()

    def write(self):
        deque.append("Terry")
        deque.append("Graham")


def initArr():
    initList = []
    for i in range(3, 10):
        initList.append(i)

    initList.insert(0, 10)
    print(initList)


def foo():
    return 3, 5.5


alpha, beta = foo()
x = foo()[1]


def reverseOrder():
    a = [1, 2, 3, 4]
    a[::-1]
    print(a)


if __name__ == "__main__":
    BaseListTest()

    li = ListTest()
    li.get()
    print(" --------------------------")
    li.append()
    print(" --------------------------")
    li.append1()
    li._del()

    s = StackTest(["b", "bb"])
    s.enterStack("a")
    s.enterStack("a1")
    s.enterStack("a11")
    s.enterStack("a2")

    print(s.readStactTop())
    print(s.popStactTopElement())

    alpha, beta = foo()
    print(alpha, beta)
    print(foo()[1])
    reverseOrder()
