# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/5
@function: python实现队列
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        """判断队列是否为空，是否有头部链点"""
        return self.front is None

    def enqueue(self, x):
        """入队列
        如果队列是空的，队列头部和尾部都是新节点；
        如果队列不是空的，加到尾部节点之后，然后更新尾部节点
        """
        node = ListNode(x)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """出队列
        从队列头部删除一个元素，并返回这个值.
        更新头部节点
        """
        if self.isEmpty():
            raise RuntimeError("The queue is empty!")
        else:
            value = self.front.val
            self.front = self.front.next
            return value

    def peek(self):
        """查看头部节点"""
        if self.isEmpty():
            raise RuntimeError("The queue is empty!")
        else:
            return self.front.val

    def printQueue(self):
        """控制台输出队列"""
        temp = self.front
        myQueue = []
        while temp is not None:
            myQueue.append(temp.val)
            temp = temp.next
        print(myQueue)


class QueueArray:
    def __init__(self):
        self.entries = []  # 队列内的参数
        self.length = 0  # 队列长度
        self.front = 0  # 队列头部位置

    def enqueue(self, x):
        """入列"""
        self.entries.append(x)
        self.length += 1

    def dequeue(self):
        """出列"""
        self.length -= 1
        dequeued = self.entries[self.front]
        self.entries = self.entries[self.front + 1:]
        return dequeued

    def isEmpty(self):
        return self.length == 0

    def peek(self):
        return self.entries[0]


queue = QueueArray()
queue.enqueue(12)
queue.enqueue(34)
queue.enqueue("abd")
queue.enqueue(999)

print(queue.entries)
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
