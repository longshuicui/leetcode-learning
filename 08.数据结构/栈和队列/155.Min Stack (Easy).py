# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/4
@function:
155. Min Stack (Easy)
https://leetcode.com/problems/min-stack/

题目描述
    设计一个最小栈，除了需要支持常规栈的操作外，还需要支持在  O(1) 时间内 查询 栈内最小值的功能。
题解
    额外建立一个新栈，栈顶表示原栈里的最小值。每当在原栈里插入一个数字时，若该数字小于等于新栈栈顶，
    则表示这个数字在原栈里是最小值，我们将其同时插入到新栈内。每当从原栈里取出一个值，若该数字等于
    新栈栈顶，则表示这个数是原栈的最小值之一，同时取出新栈栈顶
    第二种方法：每次插入原栈时，都向新栈插入一次原栈里所有值的最小值（新栈栈顶和待插入值较小的那一个），
    每次从原栈取出数据时，同样取出新栈的栈顶。这样可以避免判断
"""


class Stack:

    def __init__(self):
        """初始化栈为一个空列表"""
        self.items = []

    def isEmpty(self):
        """判断栈是否为空，返回bool值"""
        return len(self.items) == 0

    def peek(self):
        """返回栈顶元素,也就是最后一个元素"""
        return self.items[-1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)

    def push(self, item):
        """将新的元素堆进栈里面。入栈"""
        self.items.append(item)

    def pop(self):
        """出栈"""
        return self.items.pop()


class MinStack:
    def __init__(self):
        self.s = Stack()
        self.minS = Stack()

    def push(self, x):
        self.s.push(x)
        if self.minS.isEmpty() or self.minS.peek() >= x:
            self.minS.push(x)

    def pop(self):
        if not self.minS.isEmpty() and self.s.peek() == self.minS.peek():
            self.minS.pop()
        self.s.pop()

    def top(self):
        return self.s.peek()

    def getMin(self):
        return self.minS.peek()



s=MinStack()
s.push(-2)
s.push(0)
s.push(1)
s.push(-3)


print(s.getMin())
print(s.pop())
print(s.top())
print(s.getMin())
