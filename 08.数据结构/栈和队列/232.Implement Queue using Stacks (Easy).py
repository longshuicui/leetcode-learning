# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/4
@function:
232. Implement Queue using Stacks (Easy)
https://leetcode.com/problems/implement-queue-using-stacks/
题目描述
    尝试使用栈（stack）来实现队列（queue）。
题解
    队列是先进先出的数据结构，直观的实现方式是链表。栈是先进后出的数据结构。
    为了实现队列先进先出的特性，需要两个栈。
    将stack1中的所有元素转移到stack2中，然后新元素进入stack2，位于top位置，
    接着将所有的元素删除并push到stack1中
"""


# 先用python实现一个基础栈
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


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue. O(n)
        """
        self.s1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        T: worst-case O(n) S:O(1)
        """
        self.transfer()
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.transfer()
        return self.s2.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty. T:O(1) S:O(1)
        """
        return self.s1.isEmpty() and self.s2.isEmpty()

    def transfer(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                x = self.s1.pop()
                self.s2.push(x)


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.peek())
    print(q.pop())
