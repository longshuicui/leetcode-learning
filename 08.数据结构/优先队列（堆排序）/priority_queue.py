# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/4
@function:
优先队列
    可以在O(1)时间内获得最大值，并且在O(logn)时间内取出最大值和插入任意值
    优先队列常常用堆来实现。堆是一个完全二叉树。其父节点的值总是大于等于子节点的值。堆得实现用数组 ，
    堆的实现方法：
    核心操作是上浮和下沉 ：如果一个节点比父节点大，那么交换这两个节点；交换过后可能还会比新的父节点大，
    因此需要不断的进行比较和交换操作，这个过程叫上浮；类似的，如果一个节点比父节点小，也需要不断的向下
    比较和交换操作，这个过程叫下沉。如果一个节点有两个子节点，交换最大的子节点。
    维护的是数据结构的大于关系
"""

class PriorityQueue:
    def __init__(self,maxSize):
        """初始化一个数组，构建完全二叉树"""
        self.heap=[]
        self.maxSize=maxSize

    def top(self):
        """返回堆的根节点-最大值"""
        return self.heap[0]

    def swim(self,pos):
        """上浮"""
        while pos>1 and self.heap[pos//2]<self.heap[pos]:
            self.heap[pos//2], self.heap[pos]=self.heap[pos],self.heap[pos//2]
            pos//=2

    def sink(self,pos):
        while 2*pos<=self.maxSize:
            i=2*pos
            if i<self.maxSize and self.heap[i]<self.heap[i+1]:
                i+=1
            if self.heap[pos]>=self.heap[i]:
                break
            self.heap[pos], self.heap[i]=self.heap[i], self.heap[pos]
            pos=i

    def push(self, k):
        """插入任意值，把新的数字放在最后一位ie，然后上浮"""
        self.heap.append(k)
        self.swim(len(self.heap)-1)

    def pop(self):
        self.heap[0], self.heap[-1]=self.heap[-1], self.heap[0]
        self.heap.pop()
        self.sink(0)


queue=PriorityQueue(10)

values=[5,4,8,6,2,7,1,3]
for val in values:
    queue.push(val)

print(queue.heap)