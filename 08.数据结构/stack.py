# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/5
@function: python 实现栈
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