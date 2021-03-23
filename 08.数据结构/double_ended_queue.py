# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/3/23
@function: 双端队列
"""


class DoubleEndedQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def frontEnter(self, x):
        self.items.insert(0, x)

    def frontOuter(self):
        if self.isEmpty():
            raise ValueError("The deque is empty!")
        item = self.items.pop(0)
        return item

    def rearEnter(self, x):
        self.items.append(x)

    def rearOuter(self):
        if self.isEmpty():
            raise ValueError("The deque is empty!")
        item = self.items.pop()
        return item
